from django.apps import AppConfig


class ApiConfig(AppConfig):
    default = False
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'
