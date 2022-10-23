from django.apps import AppConfig


class SantehcomConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'santehcom'
    verbose_name = 'Сантехком'

    def ready(self):
        import santehcom.signals  # noqa
