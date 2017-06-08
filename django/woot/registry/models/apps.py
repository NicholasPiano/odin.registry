
### Django
from django.db import models

### Util
import uuid

### Models
class AuthServer(models.Model):

	### Properties
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	date_created = models.DateTimeField(auto_now_add=True)
	url = models.CharField(max_length=255)

	### Methods
	def contact(self, token):
		pass

class AppRegistry(models.Model):

	### Properties
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=255)
	date_created = models.DateTimeField(auto_now_add=True)

	### Methods
	def data(self, agent):
		return {
			'apps': {app.id: app.data(agent=agent) for app in self.apps.all()},
			'token': self.tokens.create(agent=agent).data(),
		}

class AppServer(models.Model):

	### Connections
	registry = models.ForeignKey('registry.AppRegistry', related_name='apps')
	auth_server = models.ForeignKey('registry.AuthServer', related_name='apps')

	### Properties
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=255)
	date_created = models.DateTimeField(auto_now_add=True)
	ws = models.CharField(max_length=255)

	### Methods
	def data(self):
		return {
			'ws': self.ws,
			'auth': self.auth_server.url,
			'token': self.tokens.create(agent=agent).data(),
		}