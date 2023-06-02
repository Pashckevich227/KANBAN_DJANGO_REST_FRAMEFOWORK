from rest_framework import serializers, viewsets
from .models import Board, Category, Task, Mark


class BoardSerializer(serializers.ModelSerializer):
    """
        Сериализатор для всех полей доски
    """
    class Meta:
        model = Board
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
        Сериализатор для полей (id, name, color, board) доски
    """
    class Meta:
        model = Category
        fields = ["id",
                  "name",
                  "color",
                  "board"]


class MarkSerializer(serializers.ModelSerializer):
    """
        Сериализатор для полей (id, name, color, board) метки
    """
    class Meta:
        model = Mark
        fields = ["id",
                  "name",
                  "color",
                  "board"]


class TaskSerializer(serializers.ModelSerializer):
    """
        Сериализатор, исключающий поля (create_date, deadline, category) задачи
    """
    class Meta:
        model = Task
        exclude = ['create_date', 'deadline', 'category']

    def create(self, validated_data):
        request = self.context['request']
        category_id = request.parser_context['kwargs']['pk']
        validated_data['category_id'] = category_id
        return super().create(validated_data)


class TaskGetSerializer(serializers.ModelSerializer):
    """
        Сериализатор для изменения всех полей в задачи, кроме 'create_date' и 'deadline'
    """
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['create_date', 'deadline']