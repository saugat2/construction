
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("index",views.index,name='home'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
    path("project",views.project,name='project'),
    path("blogs/<str:id>",views.blog_desc,name='blog_detail'),
]
