from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import addForm,Choice,Subjectform
from django.contrib.auth.decorators import login_required
from .models import Faculty,Level,Program,Syllabus,Specification,Subject
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


def topics(request,pk=0):
    # if request.method == "GET":
    try:
        sub = Subject.objects.get(id=pk)
        syl = Syllabus.objects.filter(Subject__id=pk)
    except Subject.DoesNotExist:
        raise Http404("Subject Does Not Exist")

    if request.method == "POST":
        ufile=request.FILES['document']
        print(ufile.name)
        sub.pdf = ufile
        sub.save()

    context={
        "subject":sub,
        "bus":syl,
    }
    return render(request,"syllabus/topics.html",context)
    


#this is detail view part 
#class SyllabusView(DetailView):
#    model=Syllabus

#class syllabusAddView(CreateView):

@login_required    
def add(request, pk=0):
    syllabus_list= Syllabus.objects.all()
    subject_list_list =[]

    for e in syllabus_list:
        sub = Subject.objects.filter(syllabus__id = e.id)
        subject_list_list.append(sub)
    
    is_popup=0
    if request.method == "GET":
        check={'condn':0}
        if pk==0:
            form = addForm()
        else:
            syllabus = Syllabus.objects.get(id=pk)
            form = addForm(instance = syllabus)
            is_popup=1;

    else: 
        check={'condn':1}
        if pk == 0:
            form = addForm(request.POST)
        else:
            syllabus = Syllabus.objects.get(id = pk)
            form = addForm(request.POST, instance=syllabus)
        if form.is_valid():
            form.save()
    return render(request,'syllabus/addsyllabus.html',{'form':form,'check':check,'syllabus_list':syllabus_list})

def addsub(request):
    if request.method == "GET":
        check={'condn':0}
        form = Subjectform()
    else:
        form = Subjectform(request.POST)
        check={'condn':1}
        if form.is_valid():
            form.save()
    return render(request,'syllabus/addsubject.html',{'form':form,'check':check})

def addspec(request):
    if request.method == "GET":
        check={'condn':0}
        form = Choice()
    else:
        form = Choice(request.POST)
        check={'condn':1}
        if form.is_valid():
            form.save()
    return render(request,'syllabus/addspecs.html',{'form':form,'check':check})

def delete(request, pk):
    syllabus = Syllabus.objects.get(id = pk)
    syllabus.delete()
    return redirect('/syllabus/add')

def pdfdelete(request, pk):
    sub = Subject.objects.get(id = pk)
    sub.pdf.delete()
    return redirect('/syllabus/')