# -*- coding: utf-8 -*-
from notes.models import Note
from django.contrib import admin
from django.contrib.contenttypes import admin as ct_admin


class NoteInline(ct_admin.GenericTabularInline):
    model = Note

admin.site.register(Note)
