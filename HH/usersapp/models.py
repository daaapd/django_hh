from django.db.models import ManyToManyField,CharField
from django.contrib.auth.models import AbstractUser

from hhapp.models import Area, Schedule

# Create your models here.
class Applicant(AbstractUser):
    text = CharField(max_length=30)
    areas = ManyToManyField(Area)
    schedule = ManyToManyField(Schedule)
