from distutils.command.upload import upload
from email.mime import image
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
import cv2
from . import color_analysis

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False,blank=True,unique=True, db_index=True,editable=False)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return f"{self.name}"
    
class Marble(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="marbles")
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug= models.SlugField(null=False,blank=True,unique=True, db_index=True,editable=False)
    category = models.ForeignKey(Category, null=True , on_delete =models.SET_NULL)
    image_color =  models.JSONField(default='[{"test"}]')
   
    
    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
         
        self.slug = slugify(self.title)
        
        super().save(*args, **kwargs)
        
        originalImage = color_analysis.renkanaliz(self.image.url) 
        self.image_color = originalImage
        
        super().save(*args, **kwargs)
    
    
