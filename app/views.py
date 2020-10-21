from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def Student_form(request):
    form=StudentForm()
    if request.method=="POST":
        form_data=StudentForm(request.POST)
        if form_data.is_valid():
            print(form_data.cleaned_data['name'])
            return HttpResponse(str(form_data.cleaned_data))
    return render(request,'studentform.html',context={'form':form})