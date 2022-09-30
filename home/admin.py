from django.contrib import admin

# Register your models here.
from . models import Blog,Gallery_image
admin.site.register(Blog)
admin.site.register(Gallery_image)