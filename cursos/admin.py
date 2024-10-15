from django.contrib import admin
from cursos.models import Course
from cursos.models import StackCourse


class StackAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CoursesAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'professor', 'data', 'stack', 'image',)
    search_fields = ('title', 'link', 'professor', 'data', 'stack',)


admin.site.register(StackCourse, StackAdmin)
admin.site.register(Course, CoursesAdmin)
