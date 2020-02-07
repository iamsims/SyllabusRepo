from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import addForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'syllabus/home.html')

def about(request):
    return render(request,'syllabus/about.html',{'title':'About'})

#this is detail view part 
#class SyllabusView(DetailView):
#    model=Syllabus

#class syllabusAddView(CreateView):

@login_required    
def add(request):
    form=addForm()
    return render(request,'syllabus/addform.html',{'form':form})


