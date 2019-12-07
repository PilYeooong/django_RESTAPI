from django.db import models
from django.contrib.auth.models import User

class Quote(models.Model):
    quote_author = models.CharField(max_length=30)
    quote_body = models.TextField()
    context = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.quote_author