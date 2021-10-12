from django.core.management.base import BaseCommand, CommandError
from researchapp.models import *

import os
import datetime
from django.utils import timezone


from settings import BLOGS_ROOT
BLOGS_SOURCE_DIR = BLOGS_ROOT





######################
# PREREQUISITES 

# 1. Blog files need to start with a date with hyphens
# 1. Blog files need to be in SOURCE_DIR
# 1. The directory is scanned to create a registry in the DB. The local directory is the master data. 
# 1. Each blog entry should contain a title and a date. Optionally, also a review flag.
# 1. The webapp uses the DB registry as an index, and the local files for the MD contents. 
# 1. Changing the title or date in the file contents REQUIRES updating the DB index 
# 1. The ID of blog entries is the file name. So new contents and same filename = update data in DB
# 1. ID is stored in the `md_file` field of Publications. The DB ID is the auto-increment number as usual.
# 1. Blogs permalink is similar to the Wordpress one, eg "/2018/11/23/exploring-scholarly-publications-via-dbpedia/"

#######################



class Command(BaseCommand):
	help = 'Running command ....'

	def add_arguments(self, parser):

		# Positional arguments
		# parser.add_argument('poll_ids', nargs='+', type=int)

		# Named (optional) arguments

		parser.add_argument(
			'--delete',
			action='store_true',
			help='Delete all blogs before adding new',
		)

		parser.add_argument(
			'--all',
			action='store_true',
			help='ReLoad all blogs entries, new and old, even if preexisting',
		)

	def handle(self, *args, **options):
		
		if options['delete']:
			delete_all_blogs()

		if options['all']:
			OVERWRITE_ALL=True
		else:
			OVERWRITE_ALL=False

		self.stdout.write("Reading...")
		counter1, counter2, counter3 = 0, 0, 0

		for f in os.listdir(BLOGS_SOURCE_DIR):
			if "-" in f:
				counter1 +=1
				# blog files need to start with a date with hyphens
				TITLE, DATE, REVIEW, PURE_MARKDOWN = parse_markdown(BLOGS_SOURCE_DIR+"/"+f)
				# print(TITLE, PURE_MARKDOWN)
				result = write_record(f, 
								TITLE, 
								DATE, 
								REVIEW,
								PURE_MARKDOWN, 
								OVERWRITE_ALL,
								)
				print(result)
				if result == "NEW": 
					counter2 +=1
				elif result == "MODIFIED":
					counter3 +=1


		# finally
		print(f"""\n# Files read: {counter1}\n# Records added: {counter2}\n# Records modified: {counter3}\n""")



def delete_all_blogs():
	"""Utility to delete all blog entries from DB
	NOTE: this does not zero the auto-IDs counter"""
	blogType = PubType.objects.get(pk=13) 
	Publication.objects.filter(pubtype=blogType).delete()
	print("***\nAll database Blog entries DELETED\n***")

	


def parse_markdown(full_file_path): 
	"""Parse the wordpress markdown export and return title and the text content. 

	Each blog entry should contain a title and a date. Optionally, also a review flag. 
	EG 

	```
	---
	title: "A test post that will not be made visible"
	date: "2021-09-07"
	review: true
	---

	Markdown contents here....
	```

	"""
	print("Parsing..: " + full_file_path)
	with open(full_file_path) as f:
		lines = f.readlines()
		text_begins_flag = 0
		PURE_MARKDOWN = ""
		REVIEW = False
		DATE = None
		for l in lines:
			if text_begins_flag == 2:
				PURE_MARKDOWN += l
			elif l == "---\n":
				text_begins_flag += 1 
			elif l.startswith("title: "):
				TITLE = l.replace("title: ", "")[1:-2] # remove quotes and newline char
			elif l.startswith("review: "):
				if "true" in l:
					REVIEW = True
			elif l.startswith("date: "):
				DATE = l.replace("date: ", "")[1:-2] # remove quotes and newline char
				DATE = datetime.datetime.strptime(DATE, "%Y-%m-%d")
				DATE = DATE.replace(tzinfo=datetime.timezone.utc).date()

		if not DATE:
			raise ValueError(f'No DATE found in post: {full_file_path}')		
		return TITLE, DATE, REVIEW, PURE_MARKDOWN
		



def write_record(FILENAMEID, TITLE, DATE, REVIEW, PURE_MARKDOWN, OVERWRITE_ALL):
	"""write a record to DB
	Input data eg:
	2006-06-29 / review-automatist-storyteller-systems-and-the-shifting-sands-of-story-by-g-davenport-and-m-murtaugh.md
	2007-09-12 / dbpedia-rocks.md
	2015-01-17 / notes-from-the-force11-annual-conference.md

	PURE_MARKDOWN: not saved to DB for now
	"""

	x1 = FILENAMEID[:10]
	x2 = FILENAMEID[11:].replace(".md", "")

	new_rec_flag = "MODIFIED"
	try:
		# if there's an object with same name, we keep that one!
		pub = Publication.objects.get(md_file=FILENAMEID)
		print("++++++++++++++++++++++++++ found existing obj:	%s"	 % (pub))
		if not OVERWRITE_ALL:
			return "SKIP"
	except:
		pub = Publication(md_file=FILENAMEID)
		pub.permalink = x1.replace("-", "/") + "/" + x2
		pub.save()
		print("======= created new obj:	  %s"  % (pub.id))
		new_rec_flag = "NEW"
	

	
	# add a legacy blog link 
	# TODO check in which cases this is necessary eg not newest entries
	# EG https://www.michelepasin.org/blog/2016/10/25/leipzig-semantics-2016-conference/index.html
	if True:
		legacy_path = "https://www.michelepasin.org/blog/" + x1.replace("-", "/") + "/" + x2 + "/index.html"
		pub.url1 = legacy_path
		pub.url1name = "Legacy Blog"

	pub.title = TITLE
	pub.journal = "Blog entry on www.michelepasin.org ."
	pub.pubdate = DATE
	blogType = PubType.objects.get(pk=13)
	pub.pubtype = blogType
	pub.review = REVIEW

	#
	pub.save()
	#

	authorMe = Person.objects.get(pk=1) 
	try:
		# if there's an object with same name, we keep that one!
		obj = Authorship.objects.get(person=authorMe, publication=pub)
	except:
		auth = Authorship(person=authorMe, publication=pub)
		auth.save()
	
	return new_rec_flag