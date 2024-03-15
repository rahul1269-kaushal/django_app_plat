from django.shortcuts import render

def home(request):
    return render(request,'questions/home.html')

def q1(request):
    return render(request,'questions/1.html')

def q2(request):
    return render(request, 'questions/2.html')
