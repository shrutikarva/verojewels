from django.contrib import admin

# Register your models here.
from .models import Article,ArtType
admin.site.register(Article)
admin.site.register(ArtType)
