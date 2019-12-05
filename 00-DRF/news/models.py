from django.db import models


class Journalist(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    biography = models.TextField(blank=True)
    
    def __str__(self):
        return f"{ self.first_name } { self.last_name }"
    
    
class Article(models.Model):
    author = models.ForeignKey(Journalist, on_delete=models.CASCADE,
                               related_name="articles")
    # author = models.CharField(max_length=50)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    body = models.TextField()
    location = models.CharField(max_length=120)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{ self.author } { self.title }"
    

class JobOffer(models.Model):
    company_name = models.CharField(max_length=50)
    company_email = models.EmailField(max_length=50)
    job_title = models.CharField(max_length=50)
    job_description = models.CharField(max_length=50)
    salary = models.IntegerField() # PositiveInterField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{ self.company_name }"