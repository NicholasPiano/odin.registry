
class Permission():
	def __init__(self, path):
		self.map = {}
		if path is not None:
			sub = self.map
			for token in path.split('.'):
				if token not in sub:
					sub[token] = {}
				sub = sub[token]
		super(Permission, self).__init__()

	def add(self, other_map):
		print(other_map)
		self.map = {**self.map, **other_map}

	def __and__(self, other):
		new = Permission()

		return Permission()
		self.add(other.map)

### Permission types
# 1. Super (Access to all permission levels on all objects)
Super = Permission('super')

# 2. SuperGroup (Access to all permission levels on all objects within a group)
SuperGroup = Permission('super.group')

# 3. Creator (Directly responible for the creation of the object)
Creator = Permission('creator')

# 4. Subject (Role or Group is the subject of the object)
Subject = Permission('subject')

# 5. Admin (Deny or permit access, remove or create the object)
AdminDenyPermitAccess = Permission('admin.deny_permit_access')
AdminRemoveCreate = Permission('admin.remove_create')
AdminAll = AdminDenyPermitAccess and AdminRemoveCreate

# 6. Editor (Ability to modify object properties, ability to create sub-objects)
EditorModify = Permission('editor.modify')
EditorModifyChild = Permission('editor.modify_child')
EditorAll = EditorModify and EditorModifyChild

# 7. Viewer (Read only access to object)
Viewer = Permission('viewer')