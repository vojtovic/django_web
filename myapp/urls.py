from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exercises/', views.ExerciseView.as_view(), name='exercise_list'),
    path('exercises/<int:pk>', views.ExerciseDetail.as_view(), name='exercise_detail'),
]

