from rest_framework_api_key.permissions import BaseHasAPIKey
from .models import EmployeeAPIKey

class HasEmployeeAPIKey(BaseHasAPIKey):
    model = EmployeeAPIKey