from django.urls import path
from .views.main_view import student_view,student_view_detail

urlpatterns = [
    path('student/',student_view),
    path('student/<int:id>/',student_view_detail)
]


