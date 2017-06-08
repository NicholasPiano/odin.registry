
### Django
from django.core.management.base import BaseCommand, CommandError

### Local
from registry.models import AuthServer, AppRegistry, AppServer

### Command
class Command(BaseCommand):
	def handle(self, *args, **kwargs):

		# create auth server
		auth = AuthServer.objects.create(ws='ws://localhost:8080')

		# create app registry
		app_registry = AppRegistry.objects.create(name='test')

		# create apps
		main_app = app_registry.apps.create(name='main', ws='ws://localhost:8000', auth_server=auth)
		chat_app = app_registry.apps.create(name='chat', ws='ws://localhost:8001', auth_server=auth)