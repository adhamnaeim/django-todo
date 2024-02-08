from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='task_list'),
    path('update_task/<str:id>/',views.update_task,name='update_task'),
    path('delete_task/<str:id>/',views.delete_task,name='delete_task')
]
