from django.http import HttpResponse
from django.shortcuts import render
from app13.models import Course, Student

def course_search(request):
    if request.method == "POST":
        cid = request.POST.get("cname")
        students = Student.objects.all()
        student_list = []
        
        for student in students:
            res =  student.enrolment.filter(id=cid)
            if res:
                student_list.append(student)
        
        if len(student_list) == 0:
            return HttpResponse("<h1>No Students Enrolled</h1>")
        return render(request, "selected_students.html", {"student_list": student_list})
    else:
        courses = Course.objects.all()
        return render(request, "course_search.html", {"courses": courses})
