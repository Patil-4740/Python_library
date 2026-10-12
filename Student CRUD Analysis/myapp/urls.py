from django.urls import path
from myapp.views import*


urlpatterns=[
    path('',login_user,name='login_user'),
    path('register',register,name='register'),

    path('insert',insert,name='insert'),
    path('show',show,name='show'),
    path('edit',edit,name='edit'),
    path('delete',delete,name='delete'),

    path('analysis',analysis,name='analysis'),
    path('student_chart',student_chart,name='student_chart')
    
]