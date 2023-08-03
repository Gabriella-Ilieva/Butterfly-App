from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'butterfly.accounts'

    def ready(self):
        import butterfly.accounts.signals
        result = super().ready()
        return result
