from django.urls import path, include
from rest_framework import routers
from .views import (BoardAllViewSet,
                    BoardDetailViewSet,
                    CategoryAllViewSet,
                    CategoryDetailViewSet,
                    )



urlpatterns = [
    path('api/v1/board/', BoardAllViewSet.as_view()),
    path('api/v1/board/<int:pk>/', BoardDetailViewSet.as_view()),
    path('api/v1/board/<int:pk>/category/', CategoryAllViewSet.as_view()),
    path('api/v1/category/<int:pk>/', CategoryDetailViewSet.as_view()),
]

