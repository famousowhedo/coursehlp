from django.urls import path
from .import views
from .views import CourseListView,CourseDetailView

urlpatterns = [
path('',CourseListView.as_view(), name='home'),
path('post/<int:pk>/',CourseDetailView.as_view(), name='post-detail'),
]