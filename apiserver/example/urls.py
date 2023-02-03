from django.urls import path, include
from .views import helloAPI

urlpatterns = [
    # example 에 오면 helloAPI를 불러라
    path('hello',helloAPI),

]