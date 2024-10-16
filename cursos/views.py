from django.shortcuts import render
from cursos.models import Course
# Create your views here.

def courses_view(request):
    cursos = Course.objects.all()
    search = request.GET.get('search')

    if search:
        cursos = cursos.filter(stack__name__icontains=search)

    return render(request,
                'couses.html',
                {'courses':  cursos}
            )
