from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class entrydetails(models.Model):
    name_student = models.CharField(max_length = 20)
    email_student = models.CharField(max_length= 50)
    entrypassword = models.CharField(max_length=20)
    repeat_entrypassword = models.CharField(max_length=20)
    original_features = models.JSONField(default=dict, null=True)