from django.db import models

# Create your models here.

class Visit(models.Model):
    # db -> table
    # id -> 
    path=models.TextField(blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
