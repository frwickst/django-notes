# -*- coding: utf-8 -*-
from notes.models import Note
from django.contrib import admin
from django.contrib.contenttypes import admin as ct_admin


class NoteInline(ct_admin.GenericTabularInline):
    model = Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_type', 'object_id', 'public', 'author', 'created', 'modified', 'trucated_content')

    def trucated_content(self, obj):
        return "%s" % (obj.content[:65] + (obj.content[65:] and ' ...'))
    trucated_content.short_description = 'Content'

admin.site.register(Note, NoteAdmin)
