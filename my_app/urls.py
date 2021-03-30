from django.urls import path
from django.contrib import admin

from . import views


app_name = 'my_app'
urlpatterns = [
    
    # ex: mysite.com/
    path('',views.home,name='home_page'),
    #path('new-search',views.new_search)
    path('new_search', views.new_search, name='new_search')
]