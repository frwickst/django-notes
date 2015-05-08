ChangeLog
=========

0.4 (frwickst)
---
- Code cleanup
- Added manager to Note model
  - Adds Note.objects.get_for_object() and get_for_objects() support
- Support models with a non-'id' field by using 'pk' instead
- Better Django 1.7, 1.8 support

Breaking changes:
- Dropped support for Django 1.6
- Remove half-completed template tag code

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
