from django.conf import settings

user_model_label = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')
