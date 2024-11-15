from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.

class categ(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('prod_cat',args=[self.slug])
        
class product(models.Model):
    name = models.CharField(max_length=9999,unique=True)
    slug = models.CharField(max_length=9999,unique=True)
    img = models.CharField(max_length=9999)
    price = models.IntegerField()
    stock = models.IntegerField()
    desc = models.TextField()
    available = models.BooleanField()
    category = models.ForeignKey(categ,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    def get_url(self):
        return reverse('details',args=[self.category.slug,self.slug])
 