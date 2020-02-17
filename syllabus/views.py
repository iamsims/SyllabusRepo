from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import addForm,Choice
from django.contrib.auth.decorators import login_required
from .models import Faculty,Level,Program,Syllabus,Specification,Subject,Topic
from django.http import Http404

def getjson(fac,lev,pro):
    fac_id = Faculty.objects.all().filter(title=fac)[0].id
    lev_id = Level.objects.all().filter(title=lev)[0].id
    pro_id = Program.objects.all().filter(title=pro)[0].id
    spec_id = Specification.objects.all().filter(faculty_id=fac_id, level_id=lev_id, program_id=pro_id)[0].id
    syllabus_id = Syllabus.objects.all().filter(specification_id=spec_id)[0].id
    return syllabus_id
# Create your views here.
def home(request):
    dic_list=[]
    check={'condn':0}
    if request.method == "GET":
        form = Choice()
        return render(request,'syllabus/home.html',{'form':form,'check':check})
    else:
        check={'condn':1} 
        form = Choice(request.POST)
        if form.is_valid():
            faculty = form.cleaned_data['faculty']
            level = form.cleaned_data['level']
            program = form.cleaned_data['program']

        s_id = getjson(faculty,level,program)
        s = Syllabus.objects.get(id=s_id)
        e = Subject.objects.all().filter(syllabus__id=s_id)  
        context={
            'form':form,
            'check':check,
            "subjects":e,
            "syllabus":s
        }      
        return render(request, 'syllabus/home.html',context)

def about(request):
    return render(request,'syllabus/about.html',{'title':'About'})


def topics(request,pk):
    try:
        sub = Subject.objects.get(id=pk)
        top = Topic.objects.all().filter(subject__id=pk)
        syl = Syllabus.objects.filter(Subject__id=pk)
    except Subject.DoesNotExist:
        raise Http404("Subject Does Not Exist")
    context={
        "subject":sub,
        "topics":top,
        "bus":syl
    }
    return render(request,"syllabus/topics.html",context)

#this is detail view part 
#class SyllabusView(DetailView):
#    model=Syllabus

#class syllabusAddView(CreateView):

@login_required    
def add(request):
    form=addForm()
    return render(request,'syllabus/addform.html',{'form':form})


