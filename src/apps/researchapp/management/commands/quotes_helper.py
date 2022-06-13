"""

Quotes Helper Scripts

$ python manage.py quotes_helper 2

NOTE: the tags modifiers need to be rerun a couple of times for all changes to be applied.

"""


from django.core.management.base import BaseCommand, CommandError

import os
import datetime
from django.utils import timezone


from portfolioapp.views_quotes import count_tags, read_all_files_data, QUOTES_SOURCE_DIR

# take the path used by webapp / override here is needed for testing purposes
QUOTES_PATH = QUOTES_SOURCE_DIR



class Command(BaseCommand):
	help = """Scripts for Quotes MD. """

	def add_arguments(self, parser):

		# NOTE INHERITED FROM BASECOMMAND CLASS
		# parser.add_argument(
		#     '-v', '--verbosity', action='store', dest='verbosity', default=1,
		#     type=int, choices=[0, 1, 2, 3],
		#     help='Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output',
		# )

		# Positional arguments
		parser.add_argument('script_number', nargs='+', type=int)

		parser.add_argument(
			'--verbose',
			action='store_true',
			help='Verbose mode',
		)

	def handle(self, *args, **options):
		
		verbose = options['verbose']

		print(f"==> QUOTES_PATH: {QUOTES_PATH}")

		#################
		# SCRIPT 1: remove tags with count of 1
		# Files are modified and overwritten
		#################
		if 1 in options['script_number']:
			print("==> SCRIPT 1: remove tags with count of 1")

			# read all tags available 
			tags = count_tags(read_all_files_data())

			# Filter dictionary by keeping elements whose keys are divisible by 2
			badtags = dict(filter(lambda elem: elem[1] == 1, tags.items()))
			badtags = [f"#{x}" for x in list(badtags.keys())]
			# print(badtags)
			# return

			# update all files
			for f in os.listdir(QUOTES_PATH):
				if f.endswith(".md"):
					do_remove_tags(f, badtags, False, verbose)


		#################
		# SCRIPT 2: remove tags by passing a list of tags
		# Files are modified and overwritten
		#################
		if 2 in options['script_number']:
			print("==> SCRIPT 2: remove tags by passing a list of tags")

			# MANUALLY define tags to remove	
			badtags = ["#ChE", "#DA", "#IL", "#LE", "#LA" "#PO", "#c", "#ty", "#Chi", "#Non", "#GLI", "#di", "#Quella", "#SIA", "#La", "#Ma", "#PI", "#PO", "#PUR", "#VOI", "#way"]

			# update all files
			for f in os.listdir(QUOTES_PATH):
				if f.endswith(".md"):
					do_remove_tags(f, badtags, False, verbose)



		#################


		print("----------\nDone")






##
##
##
# HELPERS
##
##
##





def do_remove_tags(fname, tags, trial_run=False, verbose=True):
	"""
	"""

	# opening the file in read mode
	file = open(QUOTES_PATH+fname	, "r")
	replacement = ""

	def replace_with_empty(tag, replaceval, line, fname):
		print("Reading file: "+fname)
		print("\tRemoving: "+tag)
		return line.replace(tag, replaceval)

	# ensure tags format
	for tag in tags:
		if not tag.startswith("#"):
			print("\tERROR: all tags should start with #!", tag)
			return

	# using a for loop to read each line of the file
	for line in file:
		line = line.strip()
		linecopy = line
		if line.startswith("#"):
			for tag in tags:
				# edge cases: tag at beginning and end of line!
				if line.startswith(tag + " "):
					linecopy = replace_with_empty(tag + " ", " ", line, fname)
				elif line.endswith(" " + tag):
					linecopy = replace_with_empty(" " + tag, " ", line, fname)
				else:
					tag = f" {tag} " # add space to avoid false positive
					if tag in line:
						linecopy = replace_with_empty(tag, " ", line, fname)

		replacement = replacement + linecopy + "\n"

	file.close()
	
	if not trial_run:
		# opening the file in write mode
		fout = open(QUOTES_PATH+fname, "w")
		fout.write(replacement)
		fout.close()


