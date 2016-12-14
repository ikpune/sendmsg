import json
from django.db import models

# Create your models here.
class TextMessages(models.Model):
	text_message = models.TextField(blank= False, null= False)
	created_on =   models.DateTimeField(auto_now_add = True)
	updated_on =   models.DateTimeField(auto_now  = True)