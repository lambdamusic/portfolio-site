from django.core.management.base import BaseCommand, CommandError
from researchapp.models import *

import os
import datetime
from django.utils import timezone


from settings import BLOGS_ROOT


######################
# SCRIPTS 
# 
# command containing multiple little fixes 
#######################



class Command(BaseCommand):
	help = 'Running command ....'

	def add_arguments(self, parser):

		parser.add_argument('script-number', nargs='+', type=int)

	def handle(self, *args, **options):

		# print(options['script-number'])
		print("---")

		#
		# 1 - adjusting PDF links in Publications
		#

		if options['script-number'][0] == 1:
			
			for p in Publication.objects.exclude(pubtype__id=13):

				print(p)
				
				if p.url1name == "PDF":
					print(f"""==Found PDF: {p.url1}""")
					p.pdf_url = p.url1
					p.url1 = ""
					p.url1name = ""
					p.save()

				if p.url2name == "PDF":
					print(f"""==Found PDF: {p.url2}""")
					p.pdf_url = p.url2
					p.url2 = ""
					p.url2name = ""
					p.save()

		print("---\nCompleted")
