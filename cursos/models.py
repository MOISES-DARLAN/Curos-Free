from django.db import models
class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)  
    professor = models.CharField(max_length=200, null=True, blank=True)  
    data = models.DateField(auto_now=True)
    def __str__(self):
        return self.title
