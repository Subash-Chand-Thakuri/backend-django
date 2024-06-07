from django.apps import AppConfig


class SubappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'subapp'
