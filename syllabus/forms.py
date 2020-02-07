#make syllabus adding forms here by authenticated user only...only if logged in
#login and add syllabus, while adding syllabus subject automatically gets created with certain marks

#first create for finding okay
#not okay..i'll first make form for filling.
from django import forms
from .models import Syllabus

class addForm(forms.ModelForm):
    class Meta:
        model=Syllabus
        fields='__all__'
