from django.contrib import admin
from .models import Article, Journalist, JobOffer

admin.site.register(Article)
admin.site.register(Journalist)
admin.site.register(JobOffer)
