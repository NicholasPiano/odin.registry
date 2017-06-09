
### Django
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

### Local
from registry.models import AppRegistry, Agent

### Util
from uuid import UUID
import json

def is_valid_uuid(uuid_string):
	try:
		val = UUID(uuid_string, version=4)
	except ValueError:
		return False

	return str(val) == uuid_string

### Views
def access(request, uuid):
	if request.method in ['POST', 'GET'] and is_valid_uuid(uuid):
		if AppRegistry.objects.filter(id=uuid).exists():
			# print(request.META['HTTP_USER_AGENT'])

			# create user_agent details
			agent_data = {
				'ip_address': 'hello',
				'user_agent': 'hello',
			}
			agent, agent_created = Agent.objects.get_or_create(**agent_data)

			# access app registry
			app_registry = AppRegistry.objects.get(id=uuid)
			return JsonResponse(app_registry.data(agent=agent))

	else:
		return JsonResponse({'status': 'failed'})
