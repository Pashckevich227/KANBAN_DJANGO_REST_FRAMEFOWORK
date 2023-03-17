from rest_framework import generics, viewsets
from rest_framework.decorators import action
from .models import Board, Task, Category, Mark
from .serializer import (BoardSerializer,
                         CategorySerializer)


class BoardAllViewSet(generics.ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class BoardDetailViewSet(generics.RetrieveAPIView):
    queryset = Board.objects.filter()
    serializer_class = BoardSerializer


class CategoryAllViewSet(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(board=self.kwargs["pk"])


class CategoryDetailViewSet(generics.RetrieveAPIView, generics.DestroyAPIView):
    queryset = Category.objects.filter()
    serializer_class = CategorySerializer
