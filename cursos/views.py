from django.shortcuts import render
from cursos.models import Course
# Create your views here.

def course_view(request):
    cursos = Course.objects.all()
    print(cursos)
    return render(request,
                'couses.html',
                 {'courses':  cursos}
             )
