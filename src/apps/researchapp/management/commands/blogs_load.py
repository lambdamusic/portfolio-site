from django.core.management.base import BaseCommand, CommandError
from researchapp.models import *

import os
import datetime
from django.utils import timezone

SOURCE_DIR = "/Users/michele.pasin/Dropbox/code/django/research_portal_2019/archive/wp-md-export/output"


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

	def handle(self, *args, **options):

		if options['delete']:
			delete_all_blogs()

		self.stdout.write("Reading...")

		for f in os.listdir(SOURCE_DIR):
			if "-" in f:
				DATE = f[:10]
				title_url = f[11:].replace(".md", "")
				# print(f"{date} / {title}")
				TITLE, PURE_MARKDOWN = parse_markdown(SOURCE_DIR+"/"+f)
				# print(TITLE, PURE_MARKDOWN)
				write_record(f, 
							DATE, 
							title_url, 
							TITLE, 
							PURE_MARKDOWN)




def parse_markdown(file_path): 
	"""Parse the wordpress markdown export and return title and the text content. 
	"""
	print("Parsing..: " + file_path)
	with open(file_path) as f:
		lines = f.readlines()
		text_begins_flag = 0
		PURE_MARKDOWN = ""
		for l in lines:
			if text_begins_flag == 2:
				PURE_MARKDOWN += l
			elif l == "---\n":
				text_begins_flag += 1 
			elif l.startswith("title: "):
				TITLE = l.replace("title: ", "")[1:-2] # remove quotes and newline char
		return TITLE, PURE_MARKDOWN
		




#  helper for django models
def get_or_new(model, title):
	"""helper method"""
	try:
		# if there's an object with same name, we keep that one!
		obj = model.objects.get(title=title)
		print("++++++++++++++++++++++++++ found existing obj:	%s"	 % (obj))
	except:
		obj = model(title=title)
		obj.save()
		print("======= created new obj:	  %s"  % (obj))
	return obj


def delete_all_blogs():
	blogType = PubType.objects.get(pk=13) 
	Publication.objects.filter(pubtype=blogType).delete()
	print("All Blogs DELETED")

	



def write_record(filename, date, title_url, title, pure_markdown):
	"""write a record to DB
	Input data eg:
	2006-06-29 / review-automatist-storyteller-systems-and-the-shifting-sands-of-story-by-g-davenport-and-m-murtaugh.md
	2007-09-12 / dbpedia-rocks.md
	2015-01-17 / notes-from-the-force11-annual-conference.md
	"""

	the_path = "https://www.michelepasin.org/blog/" + date.replace("-", "/") + "/" + title_url + "/index.html"
	# https://www.michelepasin.org/blog/2016/10/25/leipzig-semantics-2016-conference/index.html

	# the_title = title.replace("-", " ").capitalize()

	pub = get_or_new(Publication, title)

	blogType = PubType.objects.get(pk=13) 
	

	pub.url1 = the_path
	pub.url1name = "Legacy Blog"

	pub.url2 = filename
	pub.url2name = "MD file"

	pub.journal = "Blog entry on www.michelepasin.org ."
	pub.pubdate = datetime.datetime.strptime(date, "%Y-%m-%d").date()
	pub.pubtype = blogType
	pub.embedcode1 = pure_markdown

	pub.save()

	authorMe = Person.objects.get(pk=1) 
	try:
		# if there's an object with same name, we keep that one!
		obj = Authorship.objects.get(person=authorMe, publication=pub)
	except:
		auth = Authorship(person=authorMe, publication=pub)
		auth.save()
	
	