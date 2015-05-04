django-notes
=============

A simple application to allow you to attach notes to models.

Installation
-------------

Notes uses generic relations to handle attaching themselves to models. So installation is basically just like adding a generic relation item to your model.

1. Add 'notes' to your INSTALLED_APPS variable

2. Import the Note model:
	```python
	from notes.models import Note
	```

3. Add the note inline to your model's admin def in your admin.py file:
	```python
	from notes.admin import NoteInline
	
	class YourModelAdmin(admin.ModelAdmin):
		inlines = [NoteInline,]
	```

4. To enable easy management you can add a hook to your model:
	```python
	from notes.models import Note
	from django.contrib.contenttypes.fields import GenericRelation
	notes = GenericRelation(Note)
	```

Usage
------
Follow the steps above (including 4) and you should have access to all the notes at instance_of_yourmodel.notes_set.all():
```
object = YourModel.objects.get(pk=1)
notes_for_object = object.notes_set.all()
```

You can also fetch notes for a object instance using the notes manager like:
```python
from notes.models import Note
model_instance = MyModel.objects.get(pk=3)

notes_for_object = Note.objects.get_for_object(model_instance)
```

or for multiple instances like:
```python
from notes.models import Note
model_instance = MyModel.objects.get(pk=3)
another_instance = SomeOtherModel.objects.get(pk=12)

notes_for_both_objects = Note.objects.get_for_objects([model_instance, another_instance])
```

When fetching notes for multiple objects you can pass a `ordering` parameter and a `reverse_ordering`
parameter to set how the notes should be ordered. The `ordering` parameter should be the name of the 
a model attribute present in all models that is passed to the function.

