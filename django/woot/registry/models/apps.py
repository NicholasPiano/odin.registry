
### Django
from django.db import models

### Local
from odin.models import Model

### Models
class AuthServer(Model):

	### Properties
	ws = models.CharField(max_length=255)

	### Methods
	def contact(self, token):
		pass

class AppRegistry(Model):

	### Properties
	name = models.CharField(max_length=255)

	### Methods
	def data(self, agent=None):
		return {
			'apps': {str(app.id): app.data(agent=agent) for app in self.apps.all()},
			'token': self.tokens.create(agent=agent).data(),
		}

class AppServer(Model):

	### Connections
	registry = models.ForeignKey('registry.AppRegistry', related_name='apps')
	auth_server = models.ForeignKey('registry.AuthServer', related_name='apps')

	### Properties
	name = models.CharField(max_length=255)
	ws = models.CharField(max_length=255)

	### Methods
	def data(self, agent=None):
		return {
			'name': self.name,
			'ws': self.ws,
			'auth': self.auth_server.ws,
			'token': self.tokens.create(agent=agent).data(),
		}