from rest_framework import serializers
from .models import Movie, Review, Genre

class Genreserializer(serializers.ModelSerializer):
  class Meta:
    model = Genre
    fields = ('id', 'name')

class Movieserializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = ('id', 'title', 'audience', 'poster_url', 'description', 'genre')

class GenreDetailserializer(serializers.ModelSerializer):
  movies = Movieserializer(source="movie_set", many=True)
  class Meta:
    model = Movie
    fields = ('id', 'movies', 'name')

class Reviewserializer(serializers.ModelSerializer):
  class Meta:
    model = Review
    fields = ('id', 'content', 'score', 'movie')
