from django.urls import path
from . import views


urlpatterns = [
    path('', views.add_task, name='add_task'),
    path('profile/', views.showTaskExecutor, name='showTaskExecutor'),
    path('report/', views.Reports, name='Reports')
]