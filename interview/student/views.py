from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.db.models import Avg, Count, Q
from .models import Student, Mark


class StudentListView(ListView):
    model = Student
    template_name = 'student/student_list.html'
    context_object_name = 'students'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student/student_detail.html'
    context_object_name = 'student'


class AddStudentView(View):
    template_name = 'student/add_student.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        roll_number = request.POST.get('roll_number','')
        name = request.POST['name']
        date_of_birth = request.POST.get('date_of_birth', '')

        student = Student(roll_number=roll_number, name=name, date_of_birth=date_of_birth)
        student.save()
        messages.success(request, 'Student added successfully!')
        return redirect('student_list')


class AddMarkView(View):
    template_name = 'student/add_mark.html'

    def get(self, request, *args, **kwargs):
        student = get_object_or_404(Student, pk=kwargs['pk'])
        return render(request, self.template_name, {'student': student})

    def post(self, request, *args, **kwargs):
        student = get_object_or_404(Student, pk=kwargs['pk'])
        marks = request.POST['marks']
        mark = Mark(student=student, marks=marks)
        mark.save()
        messages.success(request, 'Mark added successfully!')
        return redirect('student_mark', pk=student.pk)


class StudentMarkView(View):
    template_name = 'student/student_mark.html'

    def get(self, request, *args, **kwargs):
        student = get_object_or_404(Student, pk=kwargs['pk'])
        marks = Mark.objects.filter(student=student)
        return render(request, self.template_name, {'student': student, 'marks': marks})


class ResultView(View):
    template_name = 'student/result.html'

    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        total_marks = Mark.objects.all().aggregate(total_marks=Count('id'))
        d_grade_count = Mark.objects.filter(grade='D').count()
        e_grade_count = Mark.objects.filter(grade='E').count()
        f_grade_count = Mark.objects.filter(grade='F').count()
        try:
            pass_percentage = ((total_marks['total_marks'] - f_grade_count) / total_marks['total_marks']) * 100
        except ZeroDivisionError:
            pass_percentage = 0
        s_grade_students = students.annotate(avg_marks=Avg('marks')).filter(avg_marks__gte=91).count()
        a_grade_students = students.annotate(avg_marks=Avg('marks')).filter(Q(avg_marks__gte=81) & Q(avg_marks__lte=90)).count()
        b_grade_students = students.annotate(avg_marks=Avg('marks')).filter(Q(avg_marks__gte=71) & Q(avg_marks__lte=80)).count()
        c_grade_students = students.annotate(avg_marks=Avg('marks')).filter(Q(avg_marks__gte=61) & Q(avg_marks__lte=70)).count()
        d_grade_students = students.annotate(avg_marks=Avg('marks')).filter(Q(avg_marks__gte=51) & Q(avg_marks__lte=60)).count()
        e_grade_students = students.annotate(avg_marks=Avg('marks')).filter(Q(avg_marks__gte=50) & Q(avg_marks__lte=55)).count()
        f_grade_students = students.annotate(avg_marks=Avg('marks')).filter(avg_marks__lt=50).count()
        context = {
        's_grade_students': s_grade_students,
        'a_grade_students': a_grade_students,
        'b_grade_students': b_grade_students,
        'c_grade_students': c_grade_students,
        'd_grade_students': d_grade_students,
        'e_grade_students': e_grade_students,
        'f_grade_students': f_grade_students,
        'pass_percentage': pass_percentage,
        }
        return render(request, self.template_name, context)


