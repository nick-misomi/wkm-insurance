from . import views
from django.urls import path
urlpatterns = [
     path('',views.articles, name="articles"),
     path('(<slug>[\w-]+)',views.article_detail, name="article_detail"),
]