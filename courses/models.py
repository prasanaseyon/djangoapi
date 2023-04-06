from django.db import models

# Create your models here.

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Course(models.Model):
    name= models.CharField(max_length=200)
    language= models.CharField(max_length=100)
    price=models.CharField(max_length=10)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.name

