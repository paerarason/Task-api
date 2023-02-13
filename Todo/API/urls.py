from django.urls import path,include
from .views import  TaskList,TaskDetail
urlpatterns=[
    path('task',TaskList.as_view()),
    path('task/<str:pk>',TaskDetail.as_view())
]