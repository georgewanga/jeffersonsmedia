import os
import random
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from products.utils import unique_slug_generator

def get_filename_ext(file_path):
    base_name = os.path.basename(file_path)
    name,ext=os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,file_name):
    new_file_name = random.randint(1,9999999999)
    name, ext = get_filename_ext(file_name)
    final_name='{new_file_name}{ext}'.format(new_file_name=new_file_name,ext=ext)
    return 'products/{new_file_name}/{final_name}'.format(new_file_name=new_file_name,final_name=final_name)


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def feature(self):
        return self.get_queryset().featured()

    def all(self):
        return self.get_queryset().active()

    def get_by_id(self,id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None
        

class Product(models.Model):
    category = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True,unique=True)
    description = models.TextField()
    size = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2,max_digits=11,default=0.00)
    bulk = models.CharField(max_length=120)
    image = models.ImageField(upload_to=upload_image_path,null=True,blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ProductManager()

    def get_absolute_url(self):
        return reverse('products:detail',kwargs={'slug': self.slug})

    def __str__(self):
        return self.category+' - '+self.title+' - '+self.description

    class Meta:
        verbose_name_plural = "Product"

def product_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver,sender=Product)
