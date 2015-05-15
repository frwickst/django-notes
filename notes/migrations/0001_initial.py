# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name='Content')),
                ('public', models.BooleanField(default=True, verbose_name='Public')),
                ('object_id', models.CharField(max_length=255, verbose_name='Object ID')),
                ('created', models.DateTimeField(verbose_name='Created', editable=False)),
                ('modified', models.DateTimeField(verbose_name='Modified', editable=False)),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'verbose_name': 'Note',
                'verbose_name_plural': 'Notes',
            },
            bases=(models.Model,),
        ),
    ]
