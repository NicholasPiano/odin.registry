
### Django
from django.db import models

### Field
class Field(models.Field):

	def __init__(self, *args, **kwargs):

		# Custom properties
		# 1. permission class
		# 2. serialization formatting: date, uuid,
		# print(self.format(), self.__dict__)

		super(Field, self).__init__(*args, **kwargs)

	def format(self):
		return str(self)

	def access(self, model, path, **kwargs):
		pass

class UUIDField(models.UUIDField, Field):
	def format(self):
		return str(self)

class DateTimeField(models.DateTimeField, Field):
	def format(self):
		return str(self)