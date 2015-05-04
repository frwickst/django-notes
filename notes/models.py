# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel

import operator


class NoteManager(models.Manager):
    def get_for_object(self, instance):
        ctype = ContentType.objects.get_for_model(instance)
        notes = self.filter(content_type=ctype, object_id=instance.pk)
        return notes

    def get_for_objects(self, instances, ordering=None, reverse_ordering=True):
        """
        Creates a list of all notes given a list of model instances.

        Note that duplicates can be present in the results if you pass the same
        instance multiple times.
        """
        notes = []

        # Create a list of all queries
        for instance in instances:
            ctype = ContentType.objects.get_for_model(instance)
            notes_queryset = self.filter(content_type=ctype, object_id=instance.pk)
            notes += notes_queryset

        if ordering:
            # Sort notes in place
            notes.sort(key=operator.attrgetter(ordering), reverse=reverse_ordering)

        return notes


class Note(TimeStampedModel):
    """
    A simple model to handle adding arbitrary numbers of notes to a generic object.
    """
    content = models.TextField(_('Content'))
    public = models.BooleanField(_('Public'), default=True)
    author = models.ForeignKey(User, blank=True, null=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.CharField(_('Object ID'), max_length=255)
    content_object = generic.GenericForeignKey()

    objects = NoteManager()

    class Meta:
        verbose_name = _('Note')
        verbose_name_plural = _('Notes')

