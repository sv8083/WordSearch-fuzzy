from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.SearchView.as_view(), name= 'search_view'),
    path('search_results/', views.FinalSearchResults.as_view(), name='get_search_results'),
    path('search/', views.AutcompleteSearchResults.as_view(), name = 'auto_search_results'),
]