

from django.urls import path
from app.views import HelloAPI

urlpatterns = [

    path('hello/', HelloAPI)
]