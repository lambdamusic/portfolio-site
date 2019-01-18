#!/usr/bin/env python
# encoding: utf-8

from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.utils.http import urlquote
from django.http import HttpResponse, HttpResponseNotFound
from django.db.models import Q
from django.template import RequestContext
from django.template.loader import select_template, get_template

from time import strftime

from render_block import render_block_to_string

from . import *  #  various settings in ==> __INIT__.PY
from .models import *

#########
# VIEWS: everything is managed using the dynamic dispatcher
# ===> (r'^'+prefix+'(?P<category>\w+)/(?P<name>\w+)/$', 'researchapp.views.dispatcher'),
# THen unless explicilty defined, the template is chosen dynamically using this formula:
# mytemplate = select_template([ "researchapp/%s/%s.html" % (category, name),
#								"researchapp/%s/default-item.html" % category,
#								'researchapp/default-item.html'])
#########


def dispatcher(request, pagename="", namedetail=""):
    """
	Generic fun that catches the two params in the url, and dispatches the right context and template
	"""
    VALID_PAGES = VALID_PAGES_RESEARCH + VALID_PAGES_STUFF

    if pagename and (pagename not in VALID_PAGES):
        return redirect('/')
    else:
        if pagename == 'code' or pagename == 'hacks' or pagename == 'software':
            # kind of a redirect
            pagename = 'code'
        mytemplate, context = get_page_contents(request, pagename, namedetail)

        context['menuitems'] = get_menu_tree()
        context['urlname'] = pagename
        # print "*" * 10, pagename, mytemplate
        if get_category(pagename):
            context['category'] = get_category(pagename)['name']

        # return render_to_response(
        #     mytemplate.render(context))

        return render_to_response(
        mytemplate, context)


def get_category(pagename):
    """
	hard coded mechanism for providing templates-names subdivision into folders
	"""
    if pagename:
        if pagename in VALID_PAGES_RESEARCH:
            return RESEARCH_CATEGORY
        elif pagename in VALID_PAGES_STUFF:
            return FREETIME_CATEGORY
        else:
            return {'name': "Error in get_category..."}
    return ""


def get_menu_tree():
    """
	Tree items are formatted this way:
		('top level', "top level url"), [('name', 'url bit')...] = short_title, urlstub
	If the top level doesn't provide a url path, we take the respective items urls as absolute ones!

	"""
    tree = [
        ((RESEARCH_CATEGORY['name'], "/"), [
            ('Papers', 'papers'),
            ('Projects', 'projects'),
            ('Speaking', 'speaking'),
            ('Contact', 'contact'),
        ]),
        ((FREETIME_CATEGORY['name'], "/"), [
            ('Blog', 'blog'),
            ('Ontologies', "ontologies"),
            ('Livecoding', "Livecoding"),
            ('Music', "Music"),
            ('Photos', 'Photos'),
            ('Videos', 'Videos'),
        ]),
    ]

    return tree



def get_page_contents(request, pagename, namedetail):
    """ from the url info decides what info we need for the relevant page to load
		The templates are searched for in this order:
		/TEMPLATESDIR/CAT_NAME/ITEM_NAME
		/TEMPLATESDIR/CAT_NAME/default-item.html
		/TEMPLATESDIR/default-item.html

	"""

    category = get_category(pagename)

    if not pagename:
        # THEN IT'S THE HOME PAGE

        # allfeeds = get_feeds()

        context = {
            'welcomepage': True,  # triggers 3 columns css
            # 'allfeeds' :	allfeeds,
        }
        return ['researchapp/welcome.html', context]

    # ==PAPERS list==

    if pagename == "papers" and not namedetail:
        # PUBLICATION PAGE
        query = request.GET.get('query', 'date')
        format = request.GET.get('format', 'html')
        return_items = get_pubs(query)
        context = {
            'return_items': return_items,
        }
        if format == 'bibtex':
            return [
                'researchapp/%s/papersbibtex.txt' % category['folder'], context
            ]
        elif format == 'txt':
            return [
                'researchapp/%s/papers-list.txt' % category['folder'], context
            ]
        else:
            return [
                'researchapp/%s/papers-list.html' % category['folder'], context
            ]

    # ==PAPERS specific==

    if pagename == "papers" and namedetail:
        # PAPERS SPECIFIC PAGE
        return_item = get_object_or_404(Publication, id=namedetail)
        pubs = list(Publication.objects.exclude(review=True))
        this_index = pubs.index(return_item)
        next = pubs[this_index + 1] if len(pubs) > (
            this_index + 1) else pubs[0]  # recursive
        prev = pubs[this_index - 1] if (this_index - 1) >= 0 else None

        try:  # bugfix after changing logic for speaking events
            pubtypegroup = return_item.pubtype.groupfk.name
        except:
            pubtypegroup = ""

        context = {
            'itemtitle': return_item.title,
            'itempubdate': return_item.pubdate,
            'summary': return_item.pub_summary(),
            'abstract': return_item.abstract,
            'all_urls': return_item.all_urls(),
            'type': pubtypegroup,
            'itemembed1': return_item.embedcode1,
            'prev': prev,
            'next': next,
        }
        mytemplate = select_template([
            "researchapp/%s/paper-item.html" % category['folder'],
            'researchapp/%s/default-item.html' % category['folder']
        ])

        return [mytemplate.template.name, context]

    # ==PROJECTS list==

    if pagename == "projects" and not namedetail:
        # PROJECTS LIST PAGE
        _format = request.GET.get('format', 'html')
        _active_tag = request.GET.get('k', 'all')
        # print active_tag

        if _format == 'txt':
            tags = []
            projects = Project.objects.all()
            templatee = 'researchapp/%s/projects-list.txt' % category['folder']

        else:
            tags = Project.all_used_tags()
            if _active_tag not in tags:
                _active_tag = "all"
                projects = Project.objects.all()
            else:
                projects = Project.objects.filter(tags__name=_active_tag)
            # templatee = 'researchapp/%s/projects-list.html' % category['folder']
            templatee = 'researchapp/%s/projects-list-tiles.html' % category[
                'folder']

        context = {
            'projects': projects,
            'tags': tags,
            'active_tag': _active_tag,
        }

        return [templatee, context]

    # ==PROJECTS specific==

    if pagename == "projects" and namedetail:
        # PROJECTS PAGE : separate from other because we have date-from and to...
        return_item = get_object_or_404(Project, urlstub=namedetail)

        projects = list(Project.objects.all())
        this_index = projects.index(return_item)

        next = projects[this_index + 1] if len(projects) > (
            this_index + 1) else projects[0]  # recursive
        prev = projects[this_index - 1] if (this_index - 1) >= 0 else None

        # load images from manually managed folder

        project_images_names = []

        project_images_dir = STATICFILES_DIRS[
            0] + "/manual_img/" + return_item.urlstub
        if os.path.exists(project_images_dir):
            for f in os.listdir(project_images_dir):
                if os.path.isfile(os.path.join(project_images_dir, f)):
                    if not f.startswith("."):
                        project_images_names += [f]

        context = {
            'next': next,
            'prev': prev,
            'project': return_item,
            'project_images_names': sorted(project_images_names),
        }
        return [
            'researchapp/%s/project-item.html' % category['folder'], context
        ]

    # ==SPEAKING list==

    if pagename == "speaking" and not namedetail:

        return_items = Publication.objects.filter(
            isspeaking=True).order_by('-pubdate')
        context = {
            'return_items': return_items,
        }
        return [
            'researchapp/%s/speaking-list.html' % category['folder'], context
        ]

    # ==CONTACT==

    if pagename == "contact":

        name = request.GET.get('name', '')
        reply_email = request.GET.get('email', '')
        message = request.GET.get('message', '')

        success = trySendEmail(name, reply_email, message)

        context = {'success': success}

        mytemplate = select_template([
            "researchapp/%s/%s.html" % (category['folder'], pagename),
            "researchapp/%s/default-item.html" % (category['folder'])
        ])
        return [mytemplate.template.name, context]

    # ==GENERIC PAGE list==

    if pagename and not namedetail and pagename not in STATIC_PAGES:
        context, items = {}, []
        # STUFF LIST PAGE
        if pagename == 'code':
            items = Software.objects.exclude(review=True).exclude(
                soft_type__name="ontology").order_by("soft_type", "-date")

        if pagename == 'ontologies':
            items = Software.objects.exclude(review=True).filter(
                soft_type__name="ontology").order_by("soft_type", "-date")

        if pagename == 'music':
            items = Item.objects.exclude(review=True).filter(
                Q(atype__name__iexact="music"))

        if pagename == 'livecoding':
            items = Item.objects.exclude(review=True).filter(
                Q(atype__name__iexact="livecoding")
                | Q(atype__name__iexact="performance"))

        if pagename == 'photos':
            # context['photoscode'] =  get_photos_preview(1)
            items = []
            items = Item.objects.exclude(review=True).filter(
                atype__name__iexact="photos")

            # http://stuvel.eu/media/flickrapi-docs/documentation/
            import flickrapi
            api_key = "6b36d6a49a7abb07d8f156bbe5562380"
            flickr = flickrapi.FlickrAPI(api_key, cache=True)
            sets = flickr.photosets_getList(user_id='76186999@N00')
            sets_list = []

            for s in sets.find('photosets').findall('photoset'):
                # tip: inspect the s object to see what methods are available
                url = "https://www.flickr.com/photos/mikele/sets/%s/" % s.get(
                    'id')
                d = (s[0].text, url, s.get('photos'))  # title, id and count
                sets_list += [d]
            context['sets_list'] = sets_list

        if pagename == 'videos':
            items = Item.objects.exclude(review=True).filter(
                atype__name__iexact="video")

        context['items'] = items

        mytemplate = select_template([
            "researchapp/%s/%s-list.html" % (category['folder'], pagename),
            "researchapp/%s/default-list.html" % category['folder'],
        ])
        return [mytemplate.template.name, context]

    # ==GENERIC PAGE Specific==

    if pagename and namedetail:
        # STUFF SPECIFIC PAGE
        if pagename == "code":
            return_item = get_object_or_404(Software, urlstub=namedetail)
            softwares = list(Software.objects.exclude(review=True))
            this_index = softwares.index(return_item)
            next = softwares[this_index + 1] if len(softwares) > (
                this_index + 1) else softwares[0]  # recursive
            prev = softwares[this_index - 1] if (this_index - 1) >= 0 else None

        elif pagename == "ontologies":
            return_item = get_object_or_404(Software, urlstub=namedetail)
            softwares = list(
                Software.objects.exclude(review=True).filter(
                    soft_type__name="ontology"))
            this_index = softwares.index(return_item)
            next = softwares[this_index + 1] if len(softwares) > (
                this_index + 1) else softwares[0]  # recursive
            prev = softwares[this_index - 1] if (this_index - 1) >= 0 else None

        else:  # VIDEO AND MUSIC : for the mom all together
            return_item = get_object_or_404(Item, urlstub=namedetail)
            # items = list(Item.objects.exclude(review=True))
            # this_index = items.index(return_item)
            # next = items[this_index+1] if len(items) > (this_index+1) else None
            # prev = items[this_index-1] if (this_index-1) >= 0 else None
            next = None
            prev = None

        context = {
            'itemtitle': return_item.title,
            'itemdesc': return_item.description,
            'itemembed1': return_item.embedcode1,
            'itemembed2': return_item.embedcode2,
            'datefrom': return_item.date,
            'all_urls': return_item.all_urls(),
            'next': next,
            'prev': prev,
        }
        mytemplate = select_template([
            "researchapp/%s/%s-item.html" % (category['folder'], pagename),
            'researchapp/%s/default-item.html' % (category['folder'], )
        ])
        return [mytemplate.template.name, context]

    else:
        # CATCH ALL SITUATION FOR STATIC PAGES
        context = {}
        mytemplate = select_template([
            "researchapp/%s/%s-item.html" % (category['folder'], pagename),
            'researchapp/%s/default-item.html' % (category['folder'], )
        ])
        return [mytemplate.template.name, context]


def get_pubs(query):
    """ retrieves pubs info """

    talks = PubType.objects.get(
        pk=12)  # used to exclude 'INVITED TALKS' from articles list

    if query == 'type':
        pubtypegroups_list = PubType.objects.exclude(pk=12).values_list(
            'groupfk__name').order_by('groupfk__order').distinct()
        # eg [(u'Books',), (u'Journal Articles & Book Chapters',), (u'Articles in Peer-Reviewed Conference or Proceedings',), (u'White papers, Reports, etc.',)]
        # NOTE talks are excluded as they don't have any groupfk (meta pubtype)
        return_items = []
        for x in pubtypegroups_list:
            return_items.append(
                (x[0], Publication.objects.exclude(pubtype=talks).filter(
                    pubtype__groupfk__name=x[0])))
        return return_items

    elif query == 'date':
        valid_years = list(
            set([
                x[0].year for x in Publication.objects.exclude(
                    pubtype=talks).values_list('pubdate').distinct()
            ]))
        return_items = []
        valid_years.sort(reverse=True)
        # print valid_years
        for x in valid_years:
            return_items.append((x, Publication.objects.exclude(
                pubtype=talks).filter(pubdate__year=x)))
        return return_items

    elif query == 'project':
        valid_projects = list(
            set([
                x[0] for x in Publication.objects.exclude(
                    pubtype=talks).values_list('project__title') if x[0]
            ]))
        return_items = []
        for x in valid_projects:
            return_items.append((x, Publication.objects.exclude(
                pubtype=talks).filter(project__title=x)))
        return_items.sort()  # sort by alpha
        return_items.append(('Miscellaneous',
                             Publication.objects.filter(project=None)))
        return return_items

    else:
        return None


def get_photos_preview(npictures=1):
    """
	Snippet that retrieves the html code for a random picture among the ones I preselected
	2012-09-23: TODO: fix the css in photos templates, cause if we have more than 1 image the wrapping of text is fucked....
	"""

    photoscode = ""
    photos = Item.objects.exclude(review=True).filter(
        atype__name__iexact="Photos_homepage")
    if photos:
        photoscode = photos[0].embedcode1.strip().split("****")
        now = datetime.today()
        n = now.hour * (float(len(photoscode)) / 24.0
                        )  # change pic at every hour
        # you could experiment with now.day too...

        photoscode_out = ""
        for x in range(npictures):
            try:
                photoscode_out += photoscode[int(n + x)]  # similar to floor..
            except:
                pass

        return photoscode_out


def format_feeds(allfeeds):
    """
	Does some formatting
	"""
    # add the colors to the objects we're passing back: UNUSED but still here in case...
    colors1 = interpolate("#E3E4FA", "#E0FFFF", len(allfeeds))  #background
    colors2 = interpolate("#000000", "#000000", len(allfeeds))  #color
    for n in range(0, len(allfeeds)):
        if allfeeds[n]['url'].find("twitter.com") >= 0:
            allfeeds[n]['type'] = "twitter"
        elif allfeeds[n]['url'].find("michelepasin.org/blog") >= 0:
            allfeeds[n]['type'] = "blogpost"
        elif allfeeds[n]['url'].find("/papers/") >= 0:
            allfeeds[n]['type'] = "publication"
        elif allfeeds[n]['url'].find("/videos/") >= 0:
            allfeeds[n]['type'] = "video"
        elif allfeeds[n]['url'].find("/music/") >= 0:
            allfeeds[n]['type'] = "music"
        elif allfeeds[n]['url'].find("/software/") >= 0:
            allfeeds[n]['type'] = "software"
        elif allfeeds[n]['url'].find("/projects/") >= 0:
            allfeeds[n]['type'] = "project"
        else:
            allfeeds[n]['type'] = "undefined"

        allfeeds[n]['background'] = colors1[n]
        allfeeds[n]['color'] = colors2[n]

    return allfeeds


def ajax_get_newsfeed(request):
    """
	ajax view that returns a newsfeed - rendered on welcome page async.

	"""

    allfeeds = retrieveFeeds(RSS_FEEDS, randomize=False)

    # printDebug(RSS_FEEDS)
    # printDebug(allfeeds)

    # allfeeds = format_feeds(allfeeds)

    return_str = render_block_to_string(
        'researchapp/components/newstable.html', 'newstable',
        {'allfeeds': allfeeds})
    return HttpResponse(return_str)


def ajax_get_blogs(request):
    """
	ajax view that returns blog posts

	"""

    posts = retrieveFeeds(RSS_MY_BLOG, randomize=False)

    # printDebug(RSS_FEEDS)
    # printDebug(allfeeds)

    # allfeeds = format_feeds(allfeeds)

    return_str = render_block_to_string(
        'researchapp/components/blogposts.html', 'blogposts',
        {'allfeeds': posts})
    return HttpResponse(return_str)


def trySendEmail(name, reply_email, message):
    """ sends an email"""

    from_email = "communications@michelepasin.org"
    to_email = "michele.pasin@gmail.com"

    if (name or reply_email or message):
        if name and reply_email and message:
            # then all data have been entered

            try:
                subject = "[michelepasin.org] New mail from %s " % reply_email
                message = """[This is a message sent using the contact form on michelepasin.org]\n\n

Sender: %s\n
Email: %s\n
---------------------------------\n
Message: %s\n\n

					""" % (name, reply_email, message)

                headers = {'Reply-To': reply_email}
                msg = EmailMessage(
                    subject, message, from_email, [to_email], headers=headers)
                msg.content_subtype = "html"
                msg.send()

                success = 'sent'
            except:
                success = 'error'
                pass

        else:
            # missing data in the form
            success = 'error'
    else:
        success = None

    return success
