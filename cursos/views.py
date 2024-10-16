from django.shortcuts import render, redirect
from cursos.models import Course
from cursos.forms import CourseForm
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


def new_course_view(request):
    if request.method == 'POST':
        new_course = CourseForm(request.POST, request.FILES)

        if new_course.is_valid():
            new_course.save()
            return redirect('cursos')


    new_course_form = CourseForm()
    return render(request, 'new_course.html', {'new_course_form': new_course_form})