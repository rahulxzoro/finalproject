from django.urls import path
from . import views
app_name='search'
urlpatterns = [
    path('category/',views.search,name='search'),
   
]
