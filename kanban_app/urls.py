from django.urls import path, include
from rest_framework import routers
from .views import (BoardAllViewSet,
                    BoardDetailViewSet,
                    CategoryAllViewSet,
                    CategoryDetailViewSet,
                    )



urlpatterns = [
    path('api/v1/board/', BoardAllViewSet.as_view(), name='board_list'),
    path('api/v1/board/<int:pk>/', BoardDetailViewSet.as_view(), name='board'),
    path('api/v1/board/<int:pk>/category/', CategoryAllViewSet.as_view(), name='category_list'),
    path('api/v1/category/<int:pk>/', CategoryDetailViewSet.as_view(), name='category_detail'),
]

