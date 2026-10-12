from django.shortcuts import render,redirect
from myapp.models import*
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO 
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        u=authenticate(username=username, password=password)
        if u is None:
            return render(request,'login.html',{'msg':'Invalid user credential'})
        else:
            login(request,u)
            return redirect('insert')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        username=request.POST.get('username')
        password=request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request,'register.html',{'msg':'user already exist.'})
        else:
            u=User.objects.create(first_name=f_name,last_name=l_name,username=username)
            u.set_password(password)
            u.save()
            return redirect('login_user')
    return render(request,'register.html')

def insert(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        subject=request.POST.get('subject')
        marks=request.POST.get('marks')

        Student.objects.create(name=name,email=email,age=age,subject=subject,marks=marks)
        return redirect('show')
    return render(request,'insert.html')

def show(request):
    student=Student.objects.all()
    return render(request,'show.html',{'student':student})

def edit(request):
    if request.method=='POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        subject=request.POST.get('subject')
        marks=request.POST.get('marks')

        st=Student.objects.get(pk=id)
        st.name=name
        st.email=email
        st.age=age 
        st.subject=subject 
        st.marks=marks
        st.save()
        return redirect('show')
    else:
        id=request.GET.get('id')
        st=Student.objects.get(pk=id)
    return render(request,'edit.html',{'st':st})

def delete(request):
    id=request.GET.get('id')
    st=Student.objects.get(pk=id)
    st.delete()
    return redirect('show')

def analysis(request):
    record=Student.objects.all().values('name','subject','marks')

    result=pd.DataFrame(list(record))

    if result.empty:
        stats={
            'total':0,
            'average:0'
            'highest':0,
            'lowest':0,
            'std_dev':0
        }
        subject_average=[]
    else:
        result['marks'] = result['marks'].astype(float)
        marks=result['marks'].to_numpy()

        #NumPy Calculations
        stats = {
            'total': len(result),
            'average': round(float(np.mean(marks)), 2),
            'highest': float(np.max(marks)),
            'lowest': float(np.min(marks)),
            'std_dev': round(float(np.std(marks)), 2),
        }

        #subject-wise average marks
        subject_average=(
            result.groupby('subject')['marks']
            .mean()
            .round(2)
            .reset_index()
            .to_dict('records')
        )
    return render(request,'analysis.html',{'stats':stats,'subject_average':subject_average})

def student_chart(request):
    students=Student.objects.all()
    name=[student.name for student in students]
    marks=[float(student.marks) for student in students]

    plt.figure(figsize=(8,5))
    plt.bar(name,marks)

    plt.xlabel("Name")
    plt.ylabel("Marks")
    plt.title("Student performance Analysis")
    
    plt.show()
    return HttpResponse(content_type='image/png')
    
