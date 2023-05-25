from rest_framework import mixins, viewsets
from todo.models import Todo
from todo.serializers import TodoSerializer

class TodoViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer