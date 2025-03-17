from django.apps import AppConfig


class AkauntConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'akaunt'



    def ready(self):
        import akaunt.signals

