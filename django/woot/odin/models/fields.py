
### Django
from django.db import models

### Field
class Field(models.Field):

	def __init__(self, *args, **kwargs):

		# Custom properties
		# 1. permission class
		# 2. serialization formatting: date, uuid,
		# print(self.format(), self.__dict__)
		if 'permission' in kwargs:
			self.permission = kwargs['permission']
			del kwargs['permission']

		super(Field, self).__init__(*args, **kwargs)

	def format(self):
		return str(self)

	def access(self, model, path, **kwargs):
		pass

	def check_permission(self):
		return False

# Datebase columns
class UUIDField(models.UUIDField, Field):
	def format(self):
		return str(self)

class DateTimeField(models.DateTimeField, Field):
	def format(self):
		return str(self)

class CharField(models.CharField, Field):
	def format(self):
		return str(self)

# Related objects
class ManyToOneRel(models.fields.reverse_related.ManyToOneRel, Field):
	pass

class ForeignKey(models.ForeignKey, Field):
	rel_class = ManyToOneRel

	def format(self):
		return str(self)

