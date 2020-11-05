from django.shortcuts import render
from .models import Course
from django.views.generic import ListView, DetailView
# Create your views here.

# def home(request):
#     context = {
#         'courses': Course.objects.all()
#     }
#     return render(request, 'blog/home.html',context)


class CourseListView(ListView):
    model = Course
    template_name = 'blog/home.html'
    context_object_name = 'courses'
    ordering = ['-date']
    paginate_by = 17

class CourseDetailView(DetailView):
    model = Course
      