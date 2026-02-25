import os
import sys

# Add the project directory to sys.path
sys.path.append(r'c:\django_app\django_mongo2')

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_mongo2.settings')

import django
django.setup()

from django.db.utils import load_backend
import traceback

try:
    backend = load_backend('django_mongodb_engine')
    print("Backend loaded successfully")
except Exception as e:
    print(f"FAILED to load backend: {e}")
    traceback.print_exc()
