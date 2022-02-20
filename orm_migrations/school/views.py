# from django.views.generic import ListView
from django.shortcuts import render
from school.models import Student, Teacher

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    list_student = Student.objects.all().prefetch_related('teacher')
    # list_student = Student.objects.all()
    context = {
        'object_list': list_student
    }

    # for student in list_student:
    #     print("студент - ", student)
    #     print("его учителя : ")
    #     for teach in student.teacher.all():
    #         print("Преподаватель -", teach.name)

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
