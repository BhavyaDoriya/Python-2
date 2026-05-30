from django.shortcuts import render
from app2.models import Student
# Create your views here.

def home(request):
    return render(request,"home.html") 
def about(request):
    return render(request,"about.html")
def nav(request):
    name='b1'
    score=10
    l=[1,2,"k",33,55]
    d={'name':["A","B","C"], 'age':[16,19,24]}
    
    search_term=request.GET.get('search')
    if search_term:
        students=Student.objects.filter(name__icontains=search_term)
    else:
        students=Student.objects.all()
    return render(request,"nav.html",{'n':name,'s':score,'l':l,"d":d,"students":students})