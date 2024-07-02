from django.shortcuts import render

def showlist(request):
    students = ["Tony", "Mony", "Sony", "Bob"]
    fruits = ["Mango", "Banana", "Apple", "Jackfruit"]
    return render(request, 'showlist.html',{"fruits": fruits, "students": students})
