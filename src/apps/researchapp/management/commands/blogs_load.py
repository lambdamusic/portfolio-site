from django.core.management.base import BaseCommand, CommandError
from researchapp.models import *

import os
import datetime
from django.utils import timezone

SOURCE_DIR = "/Users/michele.pasin/Dropbox/code/django/research_portal_2019/archive/wp-md-export/output"


class Command(BaseCommand):
	help = 'Running command ....'

	# def add_arguments(self, parser):
	# 	parser.add_argument('filename', type=str)

	def handle(self, *args, **options):

		self.stdout.write("Reading...")

		for f in os.listdir(SOURCE_DIR):
			if "-" in f:
				date = f[:10]
				title = f[11:].replace(".md", "")
				print(f"{date} / {title}")
				write_record(date, title)


		




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



def write_record(date, title):
	"""write a record to DB
	Input data eg:
	2006-06-29 / review-automatist-storyteller-systems-and-the-shifting-sands-of-story-by-g-davenport-and-m-murtaugh.md
	2007-09-12 / dbpedia-rocks.md
	2015-01-17 / notes-from-the-force11-annual-conference.md
	"""

	the_path = "/blog/" + date.replace("-", "/") + "/" + title + "/index.html"
	# https://www.michelepasin.org/blog/2016/10/25/leipzig-semantics-2016-conference/index.html

	the_title = title.replace("-", " ").capitalize()

	print(the_path)
	print(the_title)

	pub = get_or_new(Publication, the_title)

	blogType = PubType.objects.get(pk=13) 
	

	pub.url1 = the_path
	pub.journal = "A blog on www.michelepasin.org"
	pub.pubdate = datetime.datetime.strptime(date, "%Y-%m-%d").date()
	pub.pubtype = blogType

	pub.save()

	authorMe = Person.objects.get(pk=1) 
	auth = Authorship(person=authorMe, publication=pub)
	auth.save()
	