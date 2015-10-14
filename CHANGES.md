ChangeLog
=========

0.4.2 (frwickst)
---
- Include forgotten migration directory when installing

0.4.1 (frwickst)
---
- Better Django 1.8 support by removing deprecation warnings

0.4 (frwickst)
---
- Code cleanup
- Added manager to Note model
  - Adds Note.objects.get_for_object() and get_for_objects() support
- Support models with a non-'id' field by using 'pk' instead
- Better Django 1.7, 1.8 support
- Support for custom User models
- A nice admin list view
- Remove dependency on django-extensions

Breaking changes:
- Dropped support for Django 1.6
- Remove half-completed template tag code
- The 'created' and 'modified' fields now use normal Django fields
  instead of the ones supplied by TimeStampedModel in Django
  extensions.

0.3 (bellhops)
---
- Removing markup mixin junk.

0.2 (powellc)
---

- Added proper Sphix documentation and added project to readthedocs.org
- Implemented optional url configuration for handling notes in their own right
- Added views for CRUD of notes from the front-end

0.1 (powellc)
---

- initial release
