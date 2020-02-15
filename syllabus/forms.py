#make syllabus adding forms here by authenticated user only...only if logged in
#login and add syllabus, while adding syllabus subject automatically gets created with certain marks

#first create for finding okay
#not okay..i'll first make form for filling.
from django import forms
from .models import Syllabus,Specification

class addForm(forms.ModelForm):
    class Meta:
        model=Syllabus
        fields='__all__'

class Choice(forms.ModelForm):
    class Meta:
        model=Specification
        fields='__all__'

    def __init__(self,*args,**kwargs):
        super(Choice,self).__init__(*args,**kwargs)
        self.fields['faculty'].empty_label = "Select"
        self.fields['program'].empty_label = "Select"
        self.fields['level'].empty_label = "Select"
