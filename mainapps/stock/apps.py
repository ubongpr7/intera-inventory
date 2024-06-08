from django.apps import AppConfig




class StockConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainapps.stock'
    def ready(self):
        import mainapps.stock.signals