from django.urls import path
from .import views

urlpatterns = [
    path('', views.navigation, name="navigation"),
    path('student-list/', views.studentList, name="student-list"),
]
