from django.urls import path
from .views import StudentListView, StudentDetailView, AddStudentView, AddMarkView, StudentMarkView, ResultView

urlpatterns = [
    path('api/students/', StudentListView.as_view(), name='student_list'),
    path('api/student/add/', AddStudentView.as_view(), name='add_student'),
    path('api/student/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('api/student/<int:pk>/add-mark/', AddMarkView.as_view(), name='add_mark'),
    path('api/student/<int:pk>/mark/', StudentMarkView.as_view(), name='student_mark'),
    path('api/student/results/', ResultView.as_view(), name='result'),
]
