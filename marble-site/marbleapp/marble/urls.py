from django.urls import path
from . import views
# Kullanıcı tarafından istenilen urller 
urlpatterns = [
    
   path("", views.index,name="home"),
   path("index", views.index),
   path("marbles", views.marbles, name="marbles"),
   path("category/<slug:slug>",views.marbles_by_category,name="marbles_by_category"), 
   path("marbles/<slug:slug>",views.marble_details,name="marble_details"),
   
   
]

