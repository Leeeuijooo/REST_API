from django.urls import path, include
from .views import helloAPI
from .views import booksAPI
from .views import bookAPI
from .views import BookAPIMinxins
from .views import BooksAPIMinxins


urlpatterns = [
    # example 에 오면 helloAPI를 불러라
    path('hello',helloAPI),
    path('fbv/books', booksAPI),
    path('fbv/books/<int:bid>',bookAPI),
    path('mixin/books',BooksAPIMinxins.as_view()),
    path('mixin/book/<int:bid>',BookAPIMinxins.as_view()),

]