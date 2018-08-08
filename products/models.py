from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class ArtType(models.Model):
    type = models.CharField(max_length = 100)
    cover_img = CloudinaryField('image')

    def __str__(self):
        return self.type

class Article(models.Model):
    article_name = models.CharField(max_length = 500)
    article_type = models.ForeignKey(ArtType,on_delete=models.CASCADE)
    date =models.DateField(auto_now = True)
    article_image =CloudinaryField('image')
    article_desc =models.TextField()

    def __str__(self):
        return self.article_name

