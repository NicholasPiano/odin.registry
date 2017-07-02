
### Django
from django.db import models

### Local
from .fields import *

### Util
import uuid

### Manager
class Manager(models.Manager):

	### Methods
	def access(self, path, **kwargs):

		# Make a query over all models. Accesses only the field names, and then, recursively,
		# the field names of any related objects to avoid database lookups until necessary.

		pass

### Model
class Model(models.Model):

	### Manager
	objects = Manager()

	### Meta
	class Meta:
		abstract=True # Set this model as Abstract

	### Properties
	id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	@property
	def _id(self):
		return self.id.hex

	date_created = DateTimeField(auto_now_add=True)
	date_accessed = DateTimeField(auto_now=True, blank=True)
	date_updated = DateTimeField(auto_now=False, blank=True)

	### Methods
	def access(self, path, **kwargs):
		# 1. By some means, parse the path to access three pieces of information:
			# a. The UUID of the last object
			# b. The chain of related objects
			# c. The property specified, if any

		# For example:
		# clients.aa778fhg.suppliers.454l3kds.address
		# would yield:
			# a. '454l3kds'
			# b. ['clients', 'suppliers']
			# c. 'address'

		# This should look like an SQL query such as:
		# SELECT address FROM `supplier_table` WHERE `id`==`454l3kds`;

		# This would be very quick if I can pull it off. I think Django can be teased into behaving this way.
		# The current system makes multiple queries no matter what.

		# If the query is for the whole object (omits specific property), it should recursively return all children.
		# This is what happens currently.

		# 2. If the result of step 1 is a single object and kwargs['<property>'] is present,
		# Feel free to set that property on the final object.

		data = {field.name: field.access(self, path, **kwargs) for field in self.__class__._meta.get_fields()}

class PermissionsMixin():
	pass