
### Django
from django.db import models
from . import Model

### Component
class ComponentManager(models.Manager):
	pass

class Component(Model):

	### Manager
	objects = ComponentManager()

	### Properties
	name = models.CharField(max_length=255)

### ComponentInstance
class ComponentInstanceManager(models.Manager):
	pass

class ComponentInstance(Model):

	### Manager
	objects = ComponentInstanceManager()

	### Connections
	model = models.ForeignKey(Component, related_name='instances')
	parent = models.ForeignKey('self', related_name='children')

	### Methods
	def render(self):
		

		pass