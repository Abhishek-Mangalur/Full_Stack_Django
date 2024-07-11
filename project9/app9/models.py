from django.db import models
from django.forms import ModelForm

# Create your models here. 
class Student(models.Model): 
    student_usn=models.CharField(max_length=20) 
    student_name=models.CharField(max_length=100) 
    student_sem=models.IntegerField()
    def __str__(self):
        return self.student_name+"("+self.student_usn+")"

class Project(models.Model): 
    student=models.ForeignKey(Student,on_delete=models.CASCADE) 
    ptopic=models.CharField(max_length=200) 
    planguages=models.CharField(max_length=200) 
    pduration=models.IntegerField()

class ProjectReg(ModelForm): 
    required_css_class="required" 
    class Meta:
        model=Project
        fields=['student','ptopic','planguages','pduration']
