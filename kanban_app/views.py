from rest_framework import generics, viewsets
from .models import Board, Task, Category, Mark
from .serializer import (BoardSerializer,
                         CategorySerializer,
                         MarkSerializer,
                         TaskSerializer,
                         TaskGetSerializer)


# ---------------BOARD----------------
class BoardGetAllField(generics.ListAPIView):
    """
        Получить все существующие доски
    """
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class BoardRetrieveDetail(generics.RetrieveAPIView):
    """
        Получить конкретную доску по id
    """
    queryset = Board.objects.filter()
    serializer_class = BoardSerializer


# ----------------CATEGORY----------------
class CategoryGetCreate(generics.ListAPIView, generics.CreateAPIView):
    """
        Получить/Создать категорию для доски
    """
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(board=self.kwargs["pk"])


class CategoryDeleteDetail(generics.DestroyAPIView):
    """
        Удалить категорию
    """
    queryset = Category.objects.filter()
    serializer_class = CategorySerializer


# ----------------MARK----------------
class MarkCreate(generics.ListAPIView, generics.CreateAPIView):
    """
        Получить/Создать метку для конкретной колонки
    """
    serializer_class = MarkSerializer

    def get_queryset(self):
        return Mark.objects.filter(board=self.kwargs["pk"])


class MarkDelete(generics.DestroyAPIView):
    """
        Удалить метку по id доски и id метки
    """
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer

    def get_object(self):
        board_id = self.kwargs.get('pk')
        mark_id = self.kwargs.get('mark_pk')
        queryset = self.get_queryset()
        obj = generics.get_object_or_404(queryset, board_id=board_id, id=mark_id)
        return obj


# ----------------TASK----------------
class TaskCreate(generics.CreateAPIView):
    """
        Создать задачу для категории
    """
    serializer_class = TaskSerializer

    def get_queryset(self):
        category_id = self.kwargs['pk']
        queryset = Task.objects.filter(category_id=category_id)
        return queryset

    def perform_create(self, serializer):
        category_id = self.kwargs['pk']
        serializer.save(category_id=category_id)


class TaskGetAll(generics.ListAPIView):
    """
        Получить все задачи одной категории
    """
    serializer_class = TaskGetSerializer

    def get_queryset(self):
        category_id = self.kwargs['pk']
        queryset = Task.objects.filter(category_id=category_id)
        return queryset


class TaskGetOne(generics.RetrieveUpdateDestroyAPIView):
    """
        Получить/Изменить/Удалить конкретную задачу
    """
    serializer_class = TaskGetSerializer

    def get_queryset(self):
        return Task.objects.filter(id=self.kwargs["pk"])

