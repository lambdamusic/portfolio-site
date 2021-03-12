from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib import admin
from django.urls import reverse
#  NOTE: pre Django 1.10+ this is "from django.core.urlresolvers import reverse"

import datetime

# See also: https://docs.djangoproject.com/en/1.10/topics/migrations/#workflow

from researchapp.templatetags.extrafilters import *

import myutils.modelextra.mymodels as mymodels
from myutils.modelextra import mymodels as mymodels
from myutils.myutils import blank_or_string, preview_string

# from myutils.adminextra.autocomplete_tree_admin import *

######################
### AUTHORITY LISTS
######################
# note that all these AL don't have UPDATED_AT / CREATED_AT info.... they're inherited


class PubType(mymodels.EnhancedAuthorityList):
    """Type of publication: conference, journal, book etc. 
	"""
    # group = models.CharField(max_length=100, null=True, blank=True, verbose_name="{old} Group used for ordering the publications", )
    order = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Order number",
    )
    groupfk = models.ForeignKey(
        'PubTypeGroup',
        on_delete=models.PROTECT,
        verbose_name="Normalized grouping, used for visual display",
        null=True,
        blank=True)

    class Meta:
        verbose_name_plural = "Publication types"
        ordering = ['name']

    def __str__(self):
        return self.name

    # table_group = 'Authority lists'


class PubTypeGroup(mymodels.EnhancedAuthorityList):
    """Groups for the publication type: conference+journal, book+book chapter etc. 
	  Used mainly for display purposes...
	"""
    order = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Order number",
    )

    class Meta:
        verbose_name_plural = "Publication types Groups [for display purposes]"
        ordering = ['name']

    def __str__(self):
        return self.name

    # table_group = 'Authority lists'


class GenericType(mymodels.EnhancedAuthorityList):
    """Generic 'types' that I use to organize the 'Item' instances....
	"""
    order = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Order number",
    )

    class Meta:
        verbose_name_plural = "Generic types for organizing Items"
        ordering = ['name']

    def __str__(self):
        return self.name


class Tag(mymodels.EnhancedAuthorityList):
    """Generic 'types' that I use to organize the 'Item' instances....
	"""

    class Meta:
        verbose_name_plural = "Tags"
        ordering = ['name']

    def __str__(self):
        return self.name


#########################
##### MAIN WEBSITE OBJECTS
#########################



class Person(mymodels.EnhancedModel):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Name", )
    surname = models.CharField(max_length=255, null=True, blank=True, verbose_name="Surname",)
    institution = models.CharField(max_length=255, null=True, blank=True, verbose_name="Institution",)


    def get_admin_url(self):
        return reverse('admin:researchapp_person_change', args=(self.id,))

    get_admin_url.allow_tags = True


    def get_absolute_url(self):
        return reverse('researchapp:person_detail', args=[str(self.id)])

    def full_name(self):
        try:
            return "%s %s" % (self.name, self.surname)
        except: # fail silently
            return ""

    class Meta:
        ordering = ["surname"]

    class Admin(admin.ModelAdmin): #admin.ModelAdmin

        list_display = ('id','name', 'surname', 'institution')
        # list_editable = ('persondisplayname',)
        # filter_horizontal = ('location',)
        # radio_fields = {"ltbrole": admin.VERTICAL}
        list_filter = ['created_at', 'updated_at', 'editedrecord', 'review', ]
        search_fields = ['name', 'surname', 'id']
        list_display_links = ('surname',)
        fieldsets = [
         ('Administration',
          {'fields':
           [ 'editedrecord', 'review', 'internal_notes', ('created_at', 'created_by'),
             ('updated_at', 'updated_by')
            ],
          'classes': ['collapse']
          }),
         ('Main info',
          {'fields':
           ['name', 'surname', 'institution', ]
           }),
         ]

    def __str__(self):
        return self.name + " " + self.surname

    # table_order = 5




class Authorship(mymodels.TimeStampedHiddenModel):
    #factoidpersonkey = models.IntegerField()
    person = models.ForeignKey('Person', on_delete=models.CASCADE,)
    publication = models.ForeignKey(
        'Publication',
        on_delete=models.CASCADE,
    )
    order = models.IntegerField(null=True, blank=True, verbose_name="Order number",)
    class Meta:
        ordering = ['order']

    def __str__(self):
        return "%s %s" % ("id:", self.id)

class AuthorshipInline(admin.TabularInline): # admin.TabularInline	 InlineAutocompleteAdmin
    model = Authorship
    verbose_name = 'Authors'
    verbose_name_plural = 'Authors'
    # raw_id_fields = ('person', ) #'person', TOFIX
    extra = 4



class Publication(mymodels.EnhancedModel):
    authors = models.ManyToManyField(
        Person,
        through='Authorship',
        related_name='authored',
        verbose_name="authors",
    )
    pubtype = models.ForeignKey(
        'PubType',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="type of publication",
    )

    title = models.CharField(
        max_length=255,
        verbose_name="title",
    )
    journal = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="journal",
        help_text="(insert issue N and other descriptors here for now)")
    conference = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="conference",
    )
    conferenceurl = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="url of the conference",
    )

    abstract = models.TextField(
        null=True,
        blank=True,
        verbose_name="abstract",
    )

    pubplace = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="publication place",
    )
    pubdate = models.DateField(
        null=True,
        blank=True,
        verbose_name="publication date",
        help_text="(day will be stripped from public interface)")
    isactive = models.BooleanField(
        default=False,
        verbose_name="currently being worked on?",
        help_text=
        "This record will be marked as currenlty being worked on in the public interface"
    )
    isforthcoming = models.BooleanField(
        default=False,
        verbose_name="forthcoming?",
        help_text=
        "If True, please set the date to a future point so that the pub stays on top of the list!"
    )
    isspeaking = models.BooleanField(
        default=False,
        verbose_name="speaking?",
        help_text=
        "Means that this pub-item involves a talk component on my side")

    url1 = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="url1",
        )
    url1name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="url1 name",
    )
    url2 = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="url2",
        )
    url2name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="url2 name",
    )
    url3 = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="url3",
        )
    url3name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="url3 name",
    )
    extrainfo = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="extra info?",
    )

    project = models.ForeignKey(
        'Project',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="related to project",
    )

    embedcode1 = models.TextField(
        null=True,
        blank=True,
        verbose_name="embedcode1 (eg video, pictures..)",
    )

    def get_admin_url(self):
        return reverse('admin:researchapp_publication_change', args=(self.id,))

    get_admin_url.allow_tags = True


    def get_absolute_url(self):
        """
        new version / made with layout 2020-06-07
        """
        return reverse('portfolioapp:papers-detail', args=[str(self.id)])


    # method that gives all the urls in one go!
    def all_urls(self):
        ll = [(getattr(self, x[0]), getattr(self, x[1]))
              for x in (('url1', 'url1name'), ('url2', 'url2name'),
                        ('url3', 'url3name')) if getattr(self, x[0])]
        return ll

    def pub_summary(self):
        authors = printmanyauthors(self)
        title = self.title
        pubtype = self.journal or self.conference
        pubplace = self.pubplace or ""
        if self.isforthcoming:
            pubdate = "forthcoming"
        else:
            pubdate = self.pubdate.strftime("%B %Y")
        extrainfo = self.extrainfo or ""
        return "%s. %s - %s %s %s %s." % (authors, title, pubtype, pubplace,
                                          pubdate, extrainfo)


    def next_prev_pubs(self, exclude_talks=True):
        if exclude_talks:
            # talks = PubType.objects.get(
            #     pk=12)  # used to exclude 'INVITED TALKS' from articles list
            pubs = list(
                Publication.objects.exclude(review=True).exclude(pubtype__id=12))
        else:
            pubs = list(Publication.objects.exclude(review=True))

        this_index = pubs.index(self)
        next = pubs[this_index + 1] if len(pubs) > (
            this_index + 1) else pubs[0]  # back to front
        prev = pubs[this_index - 1] if (this_index - 1) >= 0 else None
        return (next, prev)


    class Meta:
        ordering = ["-pubdate"]

    class Admin(admin.ModelAdmin):  #admin.ModelAdmin

        list_display = (
            'pubdate',
            'isspeaking',
            'title',
            'pubtype',
            'journal',
            'conference',
        )
        list_editable = ('pubtype', 'isspeaking')
        # filter_horizontal = ('urls',)
        # radio_fields = {"ltbrole": admin.VERTICAL}
        list_filter = [
            'isspeaking', 'pubtype', 'project', 'created_at', 'updated_at',
            'editedrecord', 'review', 'isforthcoming'
        ]
        list_display_links = ('title', )
        search_fields = ['title', 'id']
        inlines = (AuthorshipInline, )
        fieldsets = [
            ('Administration', {
                'fields': [
                    'editedrecord', 'review', 'internal_notes',
                    ('created_at', 'created_by'), ('updated_at', 'updated_by')
                ],
                'classes': ['collapse']
            }),
            ('Main info', {
                'fields': [
                    'isspeaking',
                    'pubtype',
                    'title',
                    'journal',
                    ('conference', 'conferenceurl'),
                    'pubplace',
                    ('pubdate', 'isactive', 'isforthcoming'),
                    'extrainfo',
                    'abstract',
                    'project',
                    ('url1', 'url1name'),
                    ('url2', 'url2name'),
                    ('url3', 'url3name'),
                    'embedcode1',
                ]
            }),
        ]

    def __str__(self):
        return "%s [%s]" % (self.title, str(self.pubdate))

    # table_order = 5





def project_image_file_name(instance, filename):
    if len(filename.split(".")) > 2:  # try to keep file extension
        return '/'.join([
            'projects',
            "%s.%s" % (instance.urlstub, filename.split(".")[-1])
        ])
    else:
        return '/'.join(['projects', "%s" % (instance.urlstub)])


class Project(mymodels.EnhancedModel):

    urlstub = models.CharField(
        max_length=255, verbose_name="url stub", help_text="No spaces or dashes please")
    short_title = models.CharField(
        max_length=255,
        verbose_name="Short description",
    )

    title = models.CharField(
        max_length=255,
        verbose_name="Title",
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="description (html welcome!)", 
        help_text="Feel free to use https://html-online.com/editor",
    )
    myrole = models.TextField(
        null=True,
        blank=True,
        verbose_name="role in the project (html welcome!)",
    )
    embedcode1 = models.TextField(
        null=True,
        blank=True,
        verbose_name="embedcode1 (eg video, pictures..)",
    )
    embedcode2 = models.TextField(
        null=True,
        blank=True,
        verbose_name="embedcode2",
    )
    img = models.FileField(
        blank=True,
        upload_to=project_image_file_name,
        verbose_name="Icon",
        help_text=
        "upload an image to be used as an icon (should be of pre-determined size!)"
    )

    datefrom = models.DateField(
        null=True,
        blank=True,
        verbose_name="date from",
        help_text="(day will be stripped from public interface)")
    dateto = models.DateField(
        null=True,
        blank=True,
        verbose_name="date to",
        help_text="(day will be stripped from public interface)")
    isactive = models.BooleanField(
        default=False,
        verbose_name="currently active",
        help_text="This record will be marked as active in the public interface"
    )
    url1 = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="url1",
        )
    url1name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="url1 name",
    )
    url2 = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="url2",
        )
    url2name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="url2 name",
    )
    url3 = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="url3",
        )
    url3name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="url3 name",
    )
    extrainfo = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="extra info",
    )

    tags = models.ManyToManyField(
        'Tag',
        blank=True,
        related_name='projects',
        verbose_name="tags",
    )

    def get_admin_url(self):
        return reverse('admin:researchapp_project_change', args=(self.id,))

    get_admin_url.allow_tags = True


    def get_absolute_url(self):
        """
        new version / made with layout 2020-06-07
        """
        return reverse('portfolioapp:projects-detail', args=[str(self.urlstub)])

    # method that gives all the urls in one go!
    def all_urls(self):
        ll = [(getattr(self, x[0]), getattr(self, x[1]))
              for x in (('url1', 'url1name'), ('url2', 'url2name'),
                        ('url3', 'url3name')) if getattr(self, x[0])]
        return ll

    @classmethod
    def all_used_tags(self):
        _s = Project.objects.exclude(tags=None).values_list(
            'tags__name', flat=True).distinct()
        if _s:
            return sorted(list(set(_s)))
        else:
            return _s

    class Meta:
        ordering = ["-dateto"]

    class Admin(admin.ModelAdmin):  #admin.ModelAdmin

        list_display = ('id', 'title', 'urlstub', 'myrole', 'datefrom',
                        'dateto')
        list_editable = ('urlstub', 'myrole')
        filter_horizontal = ('tags',)
        # radio_fields = {"ltbrole": admin.VERTICAL}
        list_filter = [
            'isactive',
            'created_at',
            'updated_at',
            'editedrecord',
            'review',
        ]
        search_fields = ['title', 'id']
        list_display_links = ('title', )
        fieldsets = [
            ('Administration', {
                'fields': [
                    'editedrecord', 'review', 'internal_notes',
                    ('created_at', 'created_by'), ('updated_at', 'updated_by')
                ],
                'classes': ['collapse']
            }),
            ('Main info', {
                'fields': [
                    'urlstub', 'title', 'short_title', 'description',
                    (
                        'datefrom',
                        'dateto',
                    ), 'isactive', 'myrole'
                ]
            }),
            ('Descriptors', {
                'fields': [
                    ('url1', 'url1name'),
                    ('url2', 'url2name'),
                    ('url3', 'url3name'),
                    'img',
                    'tags',
                ]
            }),
            ('Extras', {
                'fields': [
                    'embedcode1',
                    'embedcode2',
                    'extrainfo',
                ]
            }),
        ]

    def __str__(self):
        return "%s [%s]" % (self.title, str(self.datefrom))

    # table_order = 5



def item_image_file_name(instance, filename):
    if len(filename.split(".")) > 2:  # try to keep file extension
        return '/'.join(
            ['item',
             "%s.%s" % (instance.urlstub, filename.split(".")[-1])])
    else:
        return '/'.join(['item', "%s" % (instance.urlstub)])


# a class for anything else we want to store, beyond pubs projs and soft
# I've put in here what we display in the 'freetime' section


class Item(mymodels.EnhancedModel):
    urlstub = models.CharField(
        max_length=255, verbose_name="url stub", help_text="No spaces please")
    short_title = models.CharField(
        max_length=255,
        verbose_name="short description",
    )

    title = models.CharField(
        max_length=255,
        verbose_name="title",
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="description (html welcome!)",
        help_text="Feel free to use https://html-online.com/editor"
    )
    embedcode1 = models.TextField(
        null=True,
        blank=True,
        verbose_name="embedcode1 (eg video, pictures..)",
    )
    embedcode2 = models.TextField(
        null=True,
        blank=True,
        verbose_name="embedcode2",
    )
    img = models.FileField(
        blank=True,
        upload_to=item_image_file_name,
        verbose_name="Image",
        help_text="upload an image (should be of pre-determined size!)")
    date = models.DateField(
        null=True,
        blank=True,
        verbose_name="date",
        help_text="(day will be stripped from public interface)")
    isactive = models.BooleanField(
        default=False,
        verbose_name="currently being worked on?",
        help_text="This record will be marked as active in the public interface"
    )
    url1 = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="url1",
        )
    url1name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="url1 name",
    )
    url2 = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="url2",
        )
    url2name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="url2 name",
    )
    url3 = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="url3",
        )
    url3name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="url3 name",
    )
    mp3url = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="url of mp3",
        )
    mp3name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="mp3 name",
        default="Download MP3")

    atype = models.ForeignKey(
        GenericType,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="generic type of object",
    )
    extrainfo = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="extra info?",
    )

    def get_admin_url(self):
        return reverse('admin:researchapp_item_change', args=(self.id,))

    get_admin_url.allow_tags = True


    def get_absolute_url(self):
        return reverse('researchapp:detail_page_dispatcher', args=['item', str(self.urlstub)])

    # method that gives all the urls in one go!
    def all_urls(self):
        ll = [(getattr(self, x[0]), getattr(self, x[1]))
              for x in (('url1', 'url1name'), ('url2', 'url2name'),
                        ('url3', 'url3name'), ('mp3url', 'mp3name'))
              if getattr(self, x[0])]
        return ll

    class Meta:
        ordering = ["-date"]

    class Admin(admin.ModelAdmin):  #admin.ModelAdmin

        list_display = (
            'id',
            'title',
            'urlstub',
            'short_title',
            'atype',
            'date',
        )
        list_editable = (
            'urlstub',
            'short_title',
        )
        # radio_fields = {"ltbrole": admin.VERTICAL}
        list_filter = [
            'atype',
            'updated_at',
            'created_at',
            'editedrecord',
            'review',
        ]
        search_fields = ['title', 'id']
        list_display_links = ('title', )

        fieldsets = [
            ('Administration', {
                'fields': [
                    'editedrecord', 'review', 'internal_notes',
                    ('created_at', 'created_by'), ('updated_at', 'updated_by')
                ],
                'classes': ['collapse']
            }),
            ('Main info', {
                'fields': [
                    'atype',
                    'urlstub',
                    'title',
                    'short_title',
                    'description',
                    ('date', 'isactive'),
                    ('url1', 'url1name'),
                    ('url2', 'url2name'),
                    ('url3', 'url3name'),
                    ('mp3url', 'mp3name'),
                    'img',
                    'embedcode1',
                    'embedcode2',
                    'extrainfo',
                ]
            }),
        ]

    def __str__(self):
        return "%s [%s]" % (self.title, str(self.date))
