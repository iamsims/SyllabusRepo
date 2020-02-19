from django.db import models
from . import choices
#all the models we need i think 
# Create your models here.

class Level(models.Model):
    Choices=[('11','I/I'),('12','I/II')]
    class Meta:
        verbose_name_plural='Levels'
    title =models.CharField(max_length=2,choices=Choices)
    
    def __str__(self):
        return self.title

class Faculty(models.Model):
    class Meta:
        verbose_name_plural='Faculties'
    title =models.CharField(max_length=100)
    #Faculty=models.ForeignKey(YearandSem,on_delete=models.CASCADE)
    
    def __str__(self):
           return self.title

class Program(models.Model):
    Choices=[('BE','Bachelors'),('ME','Masters')]
    class Meta:
        verbose_name_plural='Programs'
    title =models.CharField(max_length=2,choices=Choices)
    def __str__(self):
        return self.title   

class Specification(models.Model):
    class Meta:
        verbose_name_plural='Specifications'
    program =models.ForeignKey(Program,on_delete=models.CASCADE)
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    level=models.ForeignKey(Level,on_delete=models.CASCADE)
    def __str__(self):
        return (self.program.__str__() +self.faculty.__str__()+self.level.__str__())  
        

class Subject(models.Model):
    class Meta:
        verbose_name_plural='Subject'
    subject_code = models.CharField(max_length=25,null=True)
    subject_name = models.CharField(max_length=100)
    subject_type = models.CharField(choices = choices.SUBJECT_TYPE_CHOICES,max_length=20, default = 'COMPULSORY')#help_text='Compulsory')   #compulsory or elective
    Total_no_of_hours = models.DecimalField(max_digits=2,decimal_places=1)
    practical_final_total = models.IntegerField(null=True, blank=True)
    theory_final_total = models.IntegerField(null=True, blank=True)
    marks_final_total = models.IntegerField(null=True, blank=True)
    exam_type = models.CharField(choices=choices.EXAM_TYPE_CHOICES,max_length=20, default='Theory')
    #Fculty.year, Program#because smae  b=subject in different programs , with different marks

    def __str__(self):
        return self.subject_name

class Syllabus(models.Model):
    class Meta:
        verbose_name_plural='Syllabus'
    specification=models.ForeignKey(Specification,on_delete=models.CASCADE)
    Subject=models.ManyToManyField(Subject)
    total_final_marks = models.IntegerField()

    def __str__(self):
        return (self.specification.__str__())

    

