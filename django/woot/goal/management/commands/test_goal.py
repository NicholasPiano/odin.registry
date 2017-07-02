
### Django
from django.core.management.base import BaseCommand, CommandError

### Local
from goal.models import GoalParent

### Command
class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		gp, created = GoalParent.objects.get_or_create(name='test')
		print(GoalParent.objects.access())