from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.

def index(request):
    obj=Student.objects.all()
    ctx={"students":obj}
    return render(request,'index.html',ctx)