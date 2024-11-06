from django.urls import path
from boards import views

urlpatterns = [
    path('task_list/', views.TaskList.as_view(), name='task_list'),
    path('task_create/', views.TaskCreate.as_view(), name='task_create'),
    path('task_update/<int:pk>/', views.TaskUpdate.as_view(), name='task_update'),
    path('task_delete/<int:pk>/', views.TaskDelete.as_view(), name='task_delete'),
    path('task_detail/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    path('board_list/', views.BoardList.as_view(), name='board_list'),
    path('board_create/', views.BoardCreate.as_view(), name='board_create'),
    path('board_detail/<int:pk>/', views.BoardDetail.as_view(), name='board_detail'),
    path('board_delete/<int:pk>/', views.BoardDelete.as_view(), name='board_delete'),
    path('board_update/<int:pk>/', views.BoardUpdate.as_view(), name='board_update'),
    path('comment_create/', views.CommentCreate.as_view(), name='comment_create'),
    path('comment_update/<int:pk>/', views.CommentUpdate.as_view(), name='comment_update'),
    path('comment_delete/<int:pk>/', views.CommentDelete.as_view(), name='comment_delete'),
]