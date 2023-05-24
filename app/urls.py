

from django.urls import path
from app.views import HelloAPI, BookAPI

urlpatterns = [
    path('hello/', HelloAPI),
    path('books/', BookAPI.as_view())
]