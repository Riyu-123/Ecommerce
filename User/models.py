from django.db import models

# Create your models here.
class contact_form(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    message = models.TextField()
    date_contacted = models.DateTimeField(auto_now=True)