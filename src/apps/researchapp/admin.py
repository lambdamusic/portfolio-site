from django.contrib import admin
from .models import *

# admin.site.register(MyModel, MyModel.Admin)

# # ++++++++++++++++++++++++++++++
# # admin definition for AUTHORITY TABLES models
#


class TagAdmin(admin.ModelAdmin):
    """Standard admin definitions used by some auth lists"""

    def save_model(self, request, obj, form, change):
        """adds the user information when the rec is saved"""
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()

    list_display = (
        'id',
        'name',
        'description',
        'editedrecord',
        'review',
        'updated_at',
    )
    list_editable = ('name', )
    search_fields = ('name', 'id')
    list_filter = ('updated_at', 'updated_by', 'editedrecord', 'review')
    fieldsets = [
        ('Administration', {
            'fields': [
                'editedrecord', 'review', 'internal_notes',
                ('created_at', 'created_by'), ('updated_at', 'updated_by')
            ],
            'classes': ['collapse']
        }),
        ('Description', {
            'fields': ['name', 'description']
        }),
    ]


#  admin definitions for PubType and SoftType


class ObjTypesAdmin(admin.ModelAdmin):
    """Standard admin definitions used by some auth lists"""

    def save_model(self, request, obj, form, change):
        """adds the user information when the rec is saved"""
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()

    list_display = (
        'id',
        'name',
        'description',
        'order',
        'editedrecord',
        'review',
        'updated_at',
    )
    list_editable = ('order', )
    search_fields = ('name', 'id')
    list_filter = ('updated_at', 'updated_by', 'editedrecord', 'review',
                   'groupfk')
    fieldsets = [
        ('Administration', {
            'fields': [
                'editedrecord', 'review', 'internal_notes',
                ('created_at', 'created_by'), ('updated_at', 'updated_by')
            ],
            'classes': ['collapse']
        }),
        ('Description', {
            'fields': ['name', 'description', 'groupfk', 'order']
        }),
    ]


#  admin definitions for all Auth lists


class AuthListStandardAdmin(admin.ModelAdmin):
    """Standard admin definitions used by all authority lists"""

    def save_model(self, request, obj, form, change):
        """adds the user information when the rec is saved"""
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()

    list_display = (
        'id',
        'name',
        'description',
        'order',
        'editedrecord',
        'review',
        'updated_at',
    )
    list_editable = ('order', )
    search_fields = ('name', 'id')
    list_filter = (
        'updated_at',
        'updated_by',
        'editedrecord',
        'review',
    )
    fieldsets = [
        ('Administration', {
            'fields': [
                'editedrecord', 'review', 'internal_notes',
                ('created_at', 'created_by'), ('updated_at', 'updated_by')
            ],
            'classes': ['collapse']
        }),
        ('Description', {
            'fields': [
                'name',
                'description',
                'order',
            ]
        }),
    ]


# # ++++++++++++++++++++++++++++++
# # authority lists admin definition

admin.site.register(PubType, ObjTypesAdmin)

admin.site.register(PubTypeGroup, AuthListStandardAdmin)
admin.site.register(GenericType, AuthListStandardAdmin)

admin.site.register(Tag, TagAdmin)

# # ++++++++++++++++++++++++++++++
# # admin definition for main DOMAIN models
#

admin.site.register(Person, Person.Admin)
admin.site.register(Publication, Publication.Admin)
admin.site.register(Project, Project.Admin)
admin.site.register(Item, Item.Admin)