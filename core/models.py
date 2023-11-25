from django.db import models
from django.db.models.fields import CharField, EmailField, TextField


# Contact Data
class Contact(models.Model):
    name = CharField(max_length=150)
    email = EmailField(max_length=200)
    subject = CharField(max_length=250)
    message = TextField()