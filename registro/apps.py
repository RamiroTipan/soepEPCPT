from django.apps import AppConfig


class RegistroConfig(AppConfig):
    name = 'registro'
    verbose_name = 'EPCPT-ADMIN'

    def ready(self):
    	import registro.signals