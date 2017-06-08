
### Django
from django.db import models

### Util
import uuid

### Models
class Agent(models.Model):

	### Properties
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	date_created = models.DateTimeField(auto_now_add=True)
	ip_address = models.TextField()
	user_agent = models.TextField()

class RegistryToken(models.Model):

	### Connections
	registry = models.ForeignKey('registry.AppRegistry', related_name='tokens')
	agent = models.ForeignKey('registry.Agent', related_name='registry_tokens')

	### Properties
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	date_created = models.DateTimeField(auto_now_add=True)

	### Methods
	def data(self):
		return {
			'date_created': str(self.date_created),
		}

class AccessToken(models.Model):

	### Connections
	app = models.ForeignKey('registry.AppServer', related_name='tokens')
	agent = models.ForeignKey('registry.Agent', related_name='app_tokens')

	### Properties
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	date_created = models.DateTimeField(auto_now_add=True)
	is_auth_verified = models.BooleanField(default=False)
	is_app_verified = models.BooleanField(default=False)
	date_auth_verified = models.DateTimeField(auto_now_add=False, null=True)
	date_app_verified = models.DateTimeField(auto_now_add=False, null=True)

	### Methods
	def data(self):
		return {
			'date_created': str(self.date_created),
			'is_auth_verified': str(self.is_auth_verified),
			'is_app_verified': str(self.is_app_verified),
			'date_auth_verified': str(self.date_auth_verified) if self.date_auth_verified is not None else '',
			'date_app_verified': str(self.date_app_verified) if self.date_app_verified is not None else '',
		}