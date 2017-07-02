
### Odin
from odin.models import Manager, Model, fields
from odin.permission import AdminAll, Creator, Viewer

### Local
from .permission import Moderator

### Util


### Models
class GoalParent(Model):

	### Properties
	name = fields.CharField(max_length=255, permission=(Admin and Creator))

register('parents', GoalParent)

class GoalChild(Model):

	### Connections
	parent = fields.ForeignKey('goal.GoalParent', related_name='children', permission=(Admin and Moderator))

	### Properties
	name = fields.CharField(max_length=255, permission=(Admin and Creator and Moderator and not Viewer))
