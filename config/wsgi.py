import os
import sys

from django.core.wsgi import get_wsgi_application

FILE_PATH = os.path.dirname(__file__)
PROJECT_NAME = os.path.basename(FILE_PATH)

sys.path.append(os.path.dirname(FILE_PATH))
sys.path.append(FILE_PATH)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', PROJECT_NAME+'.settings')

application = get_wsgi_application()
