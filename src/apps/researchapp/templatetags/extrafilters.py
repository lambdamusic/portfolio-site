from django import template
from django.template.defaultfilters import stringfilter
import random

register = template.Library()


# ad hoc replacement for craeting valid bibtex
@register.filter(name='old_blog_url')
@stringfilter
def old_blog_url(value):
	return value.replace('/blog/', '/archived/blog/')
	
	


@register.filter
@stringfilter
def add_braces(value):
	"""adds double braces for bibtex formatting"""
	return "{"+value+"}"
	
@register.filter
@stringfilter
def add_2braces(value):
	"""adds double braces for bibtex formatting"""
	return "{{"+value+"}}"
	

# ad hoc replacement for craeting valid bibtex
@register.filter(name='replace_comma_with_and')
@stringfilter
def replace_comma_with_and(value):
	return value.replace(',', ' and ')
	
	
@register.filter(name='cut')
@stringfilter
def cut(value, arg):
	return value.replace(arg, '')



# 2010-06-24
@register.filter(name='latest_updated')
def latest_updated(lst, object_label = None):
	e = None
	if lst:
		e = lst.order_by('-updated_at')
	return e



# older stuff:
# useful in expressing values from a M2M relation: returns all of them separated by ';'
@register.filter(name='printmany')
def printmany(lst, object_label = None):
	e = ""
	if lst:
		n = len(lst)
		if not object_label:
			for x in range(n - 1):
				e += "%s; " % (lst[x])
			e += "%s" % (lst[n -1])
		else:
			for x in range(n - 1):
				label = getattr(lst[x], object_label) or getattr(lst[x], 'id')
				e += "%s; " % (label)
			label = getattr(lst[n - 1], object_label) or getattr(lst[n - 1], 'id') # returns the id if label missing
			e += "%s" % (getattr(lst[n -1], object_label))
	return e



@register.filter(name='printmanyauthors')
def printmanyauthors(pub, object_label = None):
	e = ""
	lst = pub.authorship_set.all()
	if lst:
		n = len(lst)
		if not object_label:
			for x in range(n - 1):
				e += "%s, " % (lst[x].person)
			e += "%s" % (lst[n -1].person)
		else:
			for x in range(n - 1):
				label = getattr(lst[x].person, object_label) or getattr(lst[x].person, 'id')
				e += "%s, " % (label)
			label = getattr(lst[n - 1].person, object_label) or getattr(lst[n - 1].person, 'id') # returns the id if label missing
			e += "%s" % (getattr(lst[n -1].person, object_label))
	return e
	
	
# as above, but also creates the link from the get_absolute_url method
# NEEDS THE SAFE filter too! >>>>>>> objects.all|printmany_withabsoluteurl|safe
@register.filter(name='printmany_withabsoluteurl')
def printmany_withabsoluteurl(lst, object_label = None):
	e = ""
	if lst:
		n = len(lst)
		if object_label:
			for x in range(n - 1):
				label = getattr(lst[x], object_label) or getattr(lst[x], 'id')
				e += "<a href=\"%s\">%s</a>; " % (lst[x].get_absolute_url(), label)
			label = getattr(lst[n - 1], object_label) or getattr(lst[n - 1], 'id')	
			e += "<a href=\"%s\">%s</a>" % (lst[n - 1].get_absolute_url(), getattr(lst[n - 1], object_label))
		else:
			for x in range(n - 1):
				e += "<a href=\"%s\">%s</a>; " % (lst[x].get_absolute_url(), lst[x])
			e += "<a href=\"%s\">%s</a>" % (lst[n - 1].get_absolute_url(), lst[n - 1])
		# e += "%s" % (lst[n -1])
	return e



# {{d.document|make_absolute_url:'id'|safe}}
@register.filter(name='make_absolute_url')
def make_absolute_url(obj, object_label = None):
	e = ""
	if obj:
		if object_label:
			label = getattr(obj, object_label) or getattr(obj, 'id')	
			e = "<a href=\"%s\">%s</a>" % (obj.get_absolute_url(), label)
		else:
			e = "<a href=\"%s\">%s</a>" % (obj.get_absolute_url(), obj)
	return e




# {{d.document|poms_italic:'id'|safe}}
@register.filter(name='format_tweet')
def format_tweet(entry):
	# try:
	try:
		title = entry['title']
	except:
		return ""
	s = title.replace("lambdaman: ", "")
	xx = s.split()
	for n in range(len(xx)):
		if xx[n].startswith("http://"):
			xx[n] = """<a href="%s" target="_blank">%s</a>"""  % (entry['url'], xx[n])
	s  = " ".join(xx)
	# except:
		# s = title
	return s


@register.filter(name='format_menuitem')
def format_menuitem(item):
	""" makes the initial part of the menu string bolder  """
	if item.find("/") > 0:
		stuff = "<b>%s</b> / %s" %	tuple([x.strip().upper() for x in item.split("/")])
	else:
		stuff = "<b>%s</b> / ..." % item.strip().upper()
	return stuff
	



@register.filter(name='oneof')
def oneof(bigstringa):
	""" selects a random element from list of items delimited by '**' """
	t = bigstringa.split("**")
	return random.choice(t)




@register.filter(name='eventsize')
def eventsize(num):
	""" The base size is 14 px (for past events)
		Here we return a bigger size, with max 24
		Line-height is 150 - we go up to 180 max. 
	 """
	size = 14+num
	if size > 25:
		size = 25
	lheight = 150+(num*2)
	if lheight > 190:
		lheight = 190
	return "font-size: %spx; line-height: %s%%;" % (size, lheight)




@register.filter(name='tagsize')
def tagsize(num):
	""" The base size is 14 px (for past events)
		Here we return a bigger size, with max 24
		Line-height is 150 - we go up to 180 max. 
	 """
	size = 6+num*2
	# if size > 25:
	# 	size = 25
	lheight = 50+num*2
	if lheight > 190:
		lheight = 190
	return "font-size: %spx; line-height: %s%%;" % (size, lheight)



@register.filter(name='tagsize_quotes')
def tagsize_quotes(num):
	""" The base size is 14 px (for past events)
		Here we return a bigger size, with max 24
		Line-height is 150 - we go up to 180 max. 
	 """
	size = 6+num*1
	# if size > 25:
	# 	size = 25
	lheight = 50+num*1
	if lheight > 190:
		lheight = 190
	return "font-size: %spx; line-height: %s%%;" % (size, lheight)


from urllib.parse import urlparse

@register.filter(name='url_domain')
def url_domain(uri):
	""" July 11, 2014: From a url returns only the domain part """
	domain = urlparse(uri).netloc
	return domain




import markdown

@register.filter(name='markdown')
def render_markdown(md):
	""" Render markdown in the template """
	try:
		return markdown.markdown(md, extensions=['fenced_code', 'codehilite'])
	except:
		return md





