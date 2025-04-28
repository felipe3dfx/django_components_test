from django.apps import AppConfig


class DummyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dummy'

    # def ready(self) -> None:
    #     from pdb import set_trace

    #     set_trace()

    #     from django.urls import reverse
    #     reverse("abcd")