from django import forms
from cursos.models import StackCourse, Course


# class CourseForm(forms.Form):
#     image = forms.ImageField()
#     title = forms.CharField(max_length=200)
#     stack = forms.ModelChoiceField(StackCourse.objects.all())
#     link = forms.CharField(max_length=200)
#     professor = forms.CharField(max_length=200)

#     def save(self):
#         new_course = Course(
#             title = self.cleaned_data['title'],
#             image = self.cleaned_data['image'],
#             stack = self.cleaned_data['stack'],
#             link = self.cleaned_data['link'],
#             professor = self.cleaned_data['professor']
#         )

#         new_course.save()
#         return new_course
    
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
