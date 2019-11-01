from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
  path('genres/', views.genre_list),
  path('genres/<int:id>/', views.genre_detail),
  path('movies/', views.movie_list),
  path('movies/<int:id>/', views.movie_detail),
  path('movies/<int:id>/reviews/', views.review_create),
  path('reviews/<int:id>/', views.review_detail)
]