
### Django
from django.core.wsgi import get_wsgi_application

### Util
from os import environ

### WGSI
environ.setdefault('DJANGO_SETTINGS_MODULE', 'woot.settings.development')
application = get_wsgi_application()
