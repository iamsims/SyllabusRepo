from django.shortcuts import render
from django.http import FileResponse
import  io
from reportlab.pdfgen import canvas
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import addForm,Choice
from django.contrib.auth.decorators import login_required
from .models import Faculty,Level,Program,Syllabus,Specification,Subject

def getjson(fac,lev,pro):
    fac_id = Faculty.objects.all().filter(title=fac)[0].id
    lev_id = Level.objects.all().filter(title=lev)[0].id
    pro_id = Program.objects.all().filter(title=pro)[0].id
    spec_id = Specification.objects.all().filter(faculty_id=fac_id, level_id=lev_id, program_id=pro_id)[0].id
    syllabus_id = Syllabus.objects.all().filter(specification_id=spec_id)[0].id
    return syllabus_id

# Create your views here.
def home(request):
    name=[]
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
        e = Subject.objects.all().filter(syllabus__id=s_id)
        for s in e:
           name.append(s.subject_name)          
        return render(request, 'syllabus/home.html',{'form':form,'check':check,'name':name})

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

def download(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='syllabus.pdf')

