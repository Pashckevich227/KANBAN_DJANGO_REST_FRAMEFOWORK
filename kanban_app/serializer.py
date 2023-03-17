from rest_framework import serializers, viewsets
from .models import Board, Category, Task, Mark

# color : yellow, green, red, light-blue, blue, purple, violet, orange

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id",
                  "name",
                  "color",
                  "board"]
