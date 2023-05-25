

from django.urls import path
from .views import TodoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"todo",TodoViewSet, basename='todo')
urlpatterns = router.urls

    # path('', TodoViewSet.as_view({'get':'list','post':'create'})),
