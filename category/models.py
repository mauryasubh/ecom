from django.db import models
from django.urls import reverse
# Create your models here.


class category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    desc = models.TextField(max_length=250, blank=True)
    img = models.ImageField(upload_to='photos/category', blank=True)


    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"  

    def get_url(self):
        return reverse('product_slug', args=[self.slug])

    def __str__(self):
        return self.name
    
  

 