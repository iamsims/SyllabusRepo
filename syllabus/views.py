from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Syllabus

# Create your views here.
def home(request):
    return render(request,'syllabus/home.html')

def about(request):
    return render(request,'syllabus/about.html',{'title':'About'})

class SyllabusView(DetailView):
    model=Syllabus

class syllabusAddView(CreateView):
    


