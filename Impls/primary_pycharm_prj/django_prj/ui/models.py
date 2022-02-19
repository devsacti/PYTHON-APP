from django.db import models

# Create your models here.
class t1(models.Model):
    col1 = models.IntegerField(default=0)
    col2 = models.CharField(max_length=200)
    col3 = models.DateTimeField('date published')
