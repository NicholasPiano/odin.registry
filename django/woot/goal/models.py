
### Odin
from odin.models import Manager, Model, fields
from odin.permission import AdminAll, Creator, Viewer

### Local
from .permission import Moderator

### Util


### Models
class GoalParent(Model):

	register = 'goal_parent'

	### Properties
	name = fields.CharField(max_length=255, permission=(AdminAll and Creator))

class GoalChild(Model):

	### Connections
	parent = fields.ForeignKey('goal.GoalParent', related_name='children', permission=(AdminAll and Moderator))

	### Properties
	name = fields.CharField(max_length=255, permission=(AdminAll and Creator and Moderator and not Viewer))
