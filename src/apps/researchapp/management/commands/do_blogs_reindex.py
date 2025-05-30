"""

```
./tools/blogs-reindex -h
```

# PREREQUISITES 

1. Blog files need to start with a date with hyphens
1. Blog files need to be in SOURCE_DIR
1. The directory is scanned to create a registry in the DB. The local directory is the master data. 
1. Each blog entry should contain a title and a date. Optionally, also a review flag.
1. The webapp uses the DB registry as an index, and the local files for the MD contents. 
1. Changing the title or date in the file contents REQUIRES updating the DB index 
1. The ID of blog entries is the file name, stored in `md_file` field. So new contents and same filename = update data in DB
1. ID is stored in the `md_file` field of Publications. The DB ID is the auto-increment number as usual.
1. Blogs permalink is similar to the Wordpress one, eg "/2018/11/23/exploring-scholarly-publications-via-dbpedia/"



"""


from django.core.management.base import BaseCommand, CommandError
from researchapp.models import *

import os
import datetime
from django.utils import timezone

import click

from settings import BLOGS_ROOT
BLOGS_SOURCE_DIR = BLOGS_ROOT


from myutils.myutils import printDebug


# TIP: set to True to print out extra info about tags and categories
DEBUG_TAGS = False


class Command(BaseCommand):
	help = """Reindex the blog files in BLOGS_SOURCE_DIR. For each file, parse the markdown content and add to the DB is the file is new or has changed. 
	The ID of blog entries is the file name, stored in `md_file` field. """

	def add_arguments(self, parser):

		# NOTE INHERITED FROM BASECOMMAND CLASS
        # parser.add_argument(
        #     '-v', '--verbosity', action='store', dest='verbosity', default=1,
        #     type=int, choices=[0, 1, 2, 3],
        #     help='Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output',
        # )

		parser.add_argument(
			'--resetdb',
			action='store_true',
			help='Empty all blogs entries in the Django database. NOTE: this does not zero the auto-IDs counter.',
		)

		parser.add_argument(
			'--verbose',
			action='store_true',
			help='Verbose mode',
		)

		parser.add_argument(
			'--force',
			action='store_true',
			help='Do not bother asking for validation before saving / deleting (USE WITH CAUTION).',
		)

	def handle(self, *args, **options):
		
		verbose = options['verbose']
		force = options['force']

		if options['resetdb']:
			reset_blogs_db(verbose, force)
			return 

		filenames_list = do_parse_md_folder(verbose, force)

		do_cleanup_db(filenames_list, verbose, force)

		print("----------\nDone")




def do_parse_md_folder(verbose=False, force=False):
	"""Go through the MD src folder, parse files and update the DB index if they are new/updated.

	Filenames need to be like this `2021-09-07-template-post.md`

	"""
	printDebug(f"Reading files from... <{BLOGS_SOURCE_DIR}>")
	counter1, counter2, counter3 = 0, 0, 0

	filenames_list = []

	for filename in os.listdir(BLOGS_SOURCE_DIR):

		if "-" in filename:

			filenames_list += [filename]
			counter1 +=1
			TITLE, DATE, REVIEW, CATS, TAGS, PURE_MARKDOWN = parse_markdown(BLOGS_SOURCE_DIR+"/"+filename, verbose)
			# print(TITLE, PURE_MARKDOWN)

			result = try_write_record(filename, 
										TITLE, 
										DATE, 
										CATS, 
										TAGS, 
										REVIEW,
										PURE_MARKDOWN, 
										verbose,
										force
										)
			
			if result == "NEW": 
				counter2 +=1
			elif result == "MODIFIED":
				counter3 +=1

	# finally
	printDebug(f"""\n# Files read: {counter1}\n# Records added: {counter2}\n# Records modified: {counter3}\n""", "bold")
	return(filenames_list)





def parse_markdown(full_file_path, verbose=False): 
	"""Parse the wordpress markdown export and return title and other metadata. 
	Each blog entry should contain a title and a date. Optionally, also a review flag. 

	EG 
	```
	---
	template: blog.html
	author: Michele Pasin
	title: "Composition: 'Study for Cello and Double-bass'"
	description: "A new livecoding piece using Extempore and Ableton Live."
	date: 2022-04-07
	categories: 
	- "computermusic"
	tags: 
	- "algorithmiccomposition"
	- "extempore"
	review: true
	---

	This is where the markdown content starts..
	```

	"""

	if verbose: printDebug("Parsing..: " + full_file_path)
	with open(full_file_path) as f:
		lines = f.readlines()
		text_begins_flag = cat_flag = tag_flag = 0
		PURE_MARKDOWN = ""
		REVIEW = False
		DATE = None
		CATS = []
		TAGS = []
		for l in lines:
			# printDebug(l)
			if text_begins_flag == 2:
				PURE_MARKDOWN += l
			elif l == "---\n":
				cat_flag = tag_flag = 0
				text_begins_flag += 1  # after second one, the header is over
			elif (cat_flag or tag_flag) and l.strip().startswith("-"):
				# inner categories / tags
				if cat_flag:
					thiscat = l.replace('- ', "").strip()[1:-1] # remove quotes and newline char
					if DEBUG_TAGS: printDebug(f"Cat: {thiscat}")
					CATS += [thiscat.lower()]
				elif tag_flag:
					thistag = l.replace('- ', "").strip()[1:-1] # remove quotes and newline char
					if DEBUG_TAGS: printDebug(f"Tag: {thistag}")
					TAGS += [thistag.lower()]
			elif l.startswith("title: "):
				cat_flag = tag_flag = 0
				TITLE = l.replace("title: ", "")[1:-2] # remove quotes and newline char
			elif l.startswith("review: "):
				cat_flag = tag_flag = 0
				if "true" in l:
					REVIEW = True
			elif l.startswith("date: "):
				cat_flag = tag_flag = 0
				DATE = l.replace("date: ", "") 
				if DATE[0] == "\"":
					DATE = DATE[1:-2] # remove quotes and newline char
				else:
					DATE = DATE[:-1] # remove newline char
				DATE = datetime.datetime.strptime(DATE, "%Y-%m-%d")
				DATE = DATE.replace(tzinfo=datetime.timezone.utc).date()
			elif l.startswith("categories: "):
				cat_flag, tag_flag = 1, 0
			elif l.startswith("tags: "):
				cat_flag, tag_flag = 0, 1


		if not DATE:
			raise ValueError(f'No DATE found in post: {full_file_path}')		
		return TITLE, DATE, REVIEW, CATS, TAGS, PURE_MARKDOWN
		


def reset_blogs_db(verbose=False, force=False):
	"""Utility to delete all blog entries from DB
	
	NOTE: this does not zero the auto-IDs counter
	
	"""
	blogType = PubType.objects.get(pk=13) 
	printDebug("Deleting Publications with pubtype=13 (=blog)...")
	if force or click.confirm(f"Are you sure?"):
		Publication.objects.filter(pubtype=blogType).delete()
		printDebug("***\nAll database Blog entries DELETED\n***", "bold")
		return True
	return False

	
def do_cleanup_db(filenames_list, verbose=False, force=False):
	"""Check the database for files that are not present in the Markdown folder. Delete them cause they are stale.

	filenames_list = list of `md_file` values
	"""

	blogType = PubType.objects.get(pk=13) 
	blogs = Publication.objects.filter(pubtype=blogType)
	printDebug("Cleaning db...\n")
	printDebug(f"# Records in db : {blogs.count()}", "bold")
	printDebug(f"# Markdown files: {len(filenames_list)}", "bold")
	printDebug("")
	if blogs.count() != len(filenames_list):
		for p in blogs:
			if p.md_file not in filenames_list:
				printDebug(f"Missing MD file for DB record: \n {p}", "red")
				if force or click.confirm("Delete DB record?"):
					p.delete()

	# cleanup unused tags
	for tag in Tag.objects.filter(publications=None):
		if not tag.projects.count():
			printDebug(f"Unused tag: {tag}", "red")
			if force or click.confirm("Delete tag?"):
				tag.delete()



def try_write_record(FILENAMEID, TITLE, DATE, CATS, TAGS, REVIEW, PURE_MARKDOWN, verbose=False, force=False):
	"""Write a record to DB, if it is new or modified. 
	Existing records that have same metadata are not touched, so to improve performance.

	EG filenameID: `2021-10-12-world-date-terminal.md`
	EG resulting permalink: `2021/10/12/world-date-terminal`

	NOTE PURE_MARKDOWN data: not saved to DB for now
	"""

	# split data and extensiont to create the permalink 
	x1 = FILENAMEID[:10]
	x2 = FILENAMEID[11:].replace(".md", "")

	flag = "SKIP"

	# try to infer the abstract
	try:
		ABSTRACT = next(s for s in PURE_MARKDOWN.splitlines() if s)
	except:
		print(f"PURE_MARKDOWN=\n{PURE_MARKDOWN}\nend")
		if click.confirm(f"Abstract Error for: {FILENAMEID}! Set to blank and continue?"):
			ABSTRACT = ""
		return

	try:
		# if there's an object with same name, we keep that one!

		pub = Publication.objects.get(md_file=FILENAMEID)
		if verbose: printDebug(f"\t=> found existing obj: {pub}", "green")

		if pub.title != TITLE:
			printDebug(f"=> Title has changed for: {FILENAMEID}", "red")
			if force or click.confirm(f"Update record in database?"):
				flag = "MODIFIED"
		if pub.pubdate != DATE: 
			printDebug(f"=> Date has changed for: {FILENAMEID}", "red")
			if force or click.confirm(f"Update record in database?"):
				flag = "MODIFIED"
		if pub.review != REVIEW: 
			printDebug(f"=> REVIEW has changed for: {FILENAMEID}", "red")
			if force or click.confirm(f"Update record in database?"):
				flag = "MODIFIED"

		if pub.abstract != ABSTRACT: 
			printDebug(f"=> ABSTRACT has changed for: {FILENAMEID}", "red")
			if force or click.confirm(f"Update record in database?"):
				flag = "MODIFIED"
				# print(ABSTRACT)

		test_cats = sorted([c.name for c in pub.categories.all()])
		if test_cats != sorted(CATS): 
			printDebug(f"=> CATS has changed for: {FILENAMEID}", "red")
			if DEBUG_TAGS: 
				printDebug(f"\tDB=> {test_cats}", "red")
				printDebug(f"\tMD=> {CATS}", "red")
			if force or click.confirm(f"Update record in database?"):
				flag = "MODIFIED"

		test_tags = sorted([t.name for t in pub.tags.all()])
		if test_tags != sorted(TAGS): 
			printDebug(f"=> TAGS has changed for: {FILENAMEID}", "red")
			if DEBUG_TAGS:
				printDebug(f"\tDB=> {test_tags}", "red")
				printDebug(f"\tMD=> {TAGS}", "red")
			if force or click.confirm(f"Update record in database?"):
				flag = "MODIFIED"

	except:
		# create new object if not existing

		pub = Publication(md_file=FILENAMEID)
		printDebug(f"=> Found new markdown file: {FILENAMEID}.", "red")
		if force or click.confirm(f"Add to database?"):
			pub.permalink = x1.replace("-", "/") + "/" + x2
			pub.save()
			printDebug("\t=> Created new obj: {pub}", "green")
			flag = "NEW"
	

	# TEMPORARY
	# add a legacy blog link 
	# TODO check in which cases this is necessary eg not newest entries
	# # EG https://www.michelepasin.org/blog/2016/10/25/leipzig-semantics-2016-conference/index.html
	# if True:
	# 	legacy_path = "https://www.michelepasin.org/archived/blog/" + x1.replace("-", "/") + "/" + x2 + "/index.html"
	# 	pub.url1 = legacy_path
	# 	pub.url1name = "Legacy Blog"

	if flag != "SKIP":

		# update record from markdown file data

		pub.title = TITLE
		pub.journal = "Blog entry on www.michelepasin.org ."
		pub.pubdate = DATE
		pub.abstract = ABSTRACT
		blogType = PubType.objects.get(pk=13)
		pub.pubtype = blogType
		pub.review = REVIEW

		#
		pub.save()
		#

		# add author info

		authorMe = Person.objects.get(pk=1) 
		try:
			# if there's an object with same name, we keep that one!
			obj = Authorship.objects.get(person=authorMe, publication=pub)
		except:
			auth = Authorship(person=authorMe, publication=pub)
			auth.save()

		# refresh categories
		pub.categories.clear()
		if DEBUG_TAGS: printDebug(f"=> Categories for {FILENAMEID}: {CATS}", "red")
		for cat_name in CATS:
			obj, created = BlogCategory.objects.get_or_create(
    			name=cat_name)
			printDebug(f"\tCAT=> {obj}", "green")
			pub.categories.add(obj)

		# refresh tags
		pub.tags.clear()
		if DEBUG_TAGS: printDebug(f"=> Tags for {FILENAMEID}: {TAGS}", "red")
		for tag_name in TAGS:
			obj, created = Tag.objects.get_or_create(
				name=tag_name)
			printDebug(f"\tTAG=> {obj}", "green")
			pub.tags.add(obj)

		if verbose: printDebug("\t=> Object updated from Markdown file metadata", "bold")

	return flag