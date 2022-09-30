from tkinter import image_names
from unicodedata import category
from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_id=models.AutoField
    category=models.CharField(max_length=50,default='')
    sub_category=models.CharField(max_length=60,null=True)
    blog_name=models.CharField(max_length=100)
    desc=models.CharField(max_length=5000)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="home/photos",null=True)
    class Meta:
        db_table = "home_blog"
    
    def __str__(self):
        return self.blog_name

class Gallery_image(models.Model):
    image_id=models.AutoField
    category=models.CharField(max_length=20)
    pub_date=models.DateField
    image_name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="home/gallery",null=True)
    class Meta:
        db_table = "home_gallery_image"
    
    def __str__(self):
        return self.image_name