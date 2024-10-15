from django.db import models

class StackCourse(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    image_link = models.CharField(max_length=200, default='No-image')
    stack = models.ForeignKey(StackCourse, on_delete=models.PROTECT, related_name='stack_courses')
    link = models.CharField(max_length=200)  
    professor = models.CharField(max_length=200, null=True, blank=True)  
    data = models.DateField(auto_now=True)
    def __str__(self):
        return self.title
