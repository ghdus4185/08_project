from django.shortcuts import render, get_object_or_404
from .models import Movie, Review, Genre
from rest_framework.decorators import api_view
from .serializers import Movieserializer, Reviewserializer, Genreserializer, GenreDetailserializer
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def movie_list(request):
  movies = Movie.objects.all()
  serializer = Movieserializer(movies, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, id):
  movie = get_object_or_404(Movie, id=id)
  serializer = Movieserializer(movie)
  return Response(serializer.data)

@api_view(['GET'])
def genre_list(request):
  genres = Genre.objects.all()
  serializer = Genreserializer(genres, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def genre_detail(request, id):
  genre = get_object_or_404(Genre, id=id)
  serializer = Genreserializer(genre)
  return Response(serializer.data)

@api_view(['POST'])
def review_create(request, id):
  serializer = Reviewserializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    serializer.save(movie_id=id)
  return Response({'message': "작성되었습니다!!!"})

# GET, POST, PUT, DELETE
# Read, Create, Update, Delete

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, id):
  review = get_object_or_404(Review, id=id)
  if request.method == "GET":
    serializer = Reviewserializer(review)
    return Response(serializer.data)
  elif request.method == "PUT":
    serializer = Reviewserializer(data=request.data, instance=review)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
    return Response({'message': "수정되었습니다!!!"})
  else:
    return Response({'message': "삭제되었습니다!!!"})