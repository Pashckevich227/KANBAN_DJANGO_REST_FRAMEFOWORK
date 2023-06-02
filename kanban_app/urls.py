from django.urls import path, include
from .views import (BoardGetAllField,
                    BoardRetrieveDetail,
                    CategoryGetCreate,
                    CategoryDeleteDetail,
                    MarkCreate,
                    MarkDelete,
                    TaskCreate,
                    TaskGetAll,
                    TaskGetOne)



urlpatterns = [
    path('api/v1/board/', BoardGetAllField.as_view(), name='board_list'),
    path('api/v1/board/<int:pk>/', BoardRetrieveDetail.as_view(), name='board_detail'),
    path('api/v1/board/<int:pk>/category/', CategoryGetCreate.as_view(), name='category_list'),
    path('api/v1/category/<int:pk>/', CategoryDeleteDetail.as_view(), name='category_detail'),
    path('api/v1/board/<int:pk>/mark/', MarkCreate.as_view(), name='mark_create'),
    path('api/v1/board/<int:pk>/mark/<int:mark_pk>/', MarkDelete.as_view(), name='mark_delete'),
    path('api/v1/category/<int:pk>/task/', TaskCreate.as_view(), name='task_create'),
    path('api/v1/category/<int:pk>/tasks/', TaskGetAll.as_view(), name='task_list'),
    path('api/v1/task/<int:pk>/', TaskGetOne.as_view(), name='task_get_one'),
]

