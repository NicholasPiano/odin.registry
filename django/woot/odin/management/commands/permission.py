
### Django
from django.core.management.base import BaseCommand, CommandError

### Local
from odin.permission import AdminAll, Super

### Command
class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		print(AdminAll.map)