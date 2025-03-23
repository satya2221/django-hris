from django.contrib.auth.models import User
from django.db import models

from core.models import BaseModel


# Create your models here.
class Department(BaseModel):
    name = models.CharField(max_length=255)


class DepartmentMember(BaseModel):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
