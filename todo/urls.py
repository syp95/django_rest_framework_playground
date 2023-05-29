

from django.urls import path
from .views import TodoViewSet,TodoUpdateViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"todo",TodoViewSet, basename='todo')
router.register(r"update",TodoUpdateViewSet, basename='update')
urlpatterns = router.urls

    # path('', TodoViewSet.as_view({'get':'list','post':'create'})),
