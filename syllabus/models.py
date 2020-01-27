from django.db import models

#all the models we need i think 
# Create your models here.

class Program(models.Model):
    title =models.CharField(max_length=50)
    def __str__(self):
        return self.title   

class YearandSem(models.Model):
    title =models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

class Faculty(models.Model):
    title =models.CharField(max_length=100)
    #Faculty=models.ForeignKey(YearandSem,on_delete=models.CASCADE)
    
    def __str__(self):
           return self.title

class Subject(models.Model):
    title=models.CharField(max_length=50)
    theory_internal_marks=models.IntegerField()
    theory_external_marks=models.IntegerField()
    practical_internal_marks=models.IntegerField()
    practical_external_marks=models.IntegerField()
    #Fculty.year, Program#because smae  b=subject in different programs , with different marks

    def __str__(self):
        return self.title

class Syllabus(models.Model):
    yearandsem=models.ForeignKey(YearandSem,on_delete=models.CASCADE)
    program=models.ForeignKey(Program,on_delete=models.CASCADE)
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    Subject=models.ManyToManyField(Subject)

    def __str__(self):
        return (self.yearandsem.__str__() +self.program.__str__()+self.faculty.__str__())
    

