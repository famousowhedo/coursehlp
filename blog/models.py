from django.db import models
from django.utils import timezone

# Create your models here.

class Course(models.Model):
    rating = models.CharField(max_length=12, blank=True)
    instructor_name = models.CharField(max_length=20)
    instructor_badge = models.CharField(max_length=10, blank=True)
    course_image =  models.ImageField(upload_to='images/', blank=True)
    video_lenght = models.CharField(max_length=30, blank=True)
    date = models.DateTimeField(default=timezone.now)
    Course_Title = models.CharField(max_length=200)
    Course_Subtitle = models.CharField(max_length=300)
    Language = models.CharField(max_length=80, blank=True)
    Requirement_1 = models.CharField(max_length=100, blank=True)
    Requirement_2 = models.CharField(max_length=100,  blank=True)
    Requirement_3 = models.CharField(max_length=100 , blank=True)
    Description = models.TextField()
    What_you_ll_learn_1 = models.CharField(max_length=100 , blank=True)
    What_you_ll_learn_2 = models.CharField(max_length=100, blank=True)
    What_you_ll_learn_3 = models.CharField(max_length=100, blank=True)
    link_to_course = models.URLField()

    def __str__(self):
        return self.instructor_name
    
