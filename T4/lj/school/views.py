from django.shortcuts import render,redirect
from school.models import Evaluation
# Create your views here.
def home(request):
    return render(request,"home.html")
def table(request):
    eval=Evaluation.objects.all()
    return render(request,'table.html',{"evaluation":eval})
def info(request,facid):
    eval=Evaluation.objects.get(id=facid)
    return render(request,'info.html',{"data":eval})
def form(request):
    if(request.method=="POST"):
        name=request.POST.get('fac_name')
        score=request.POST.get('score')
        sub=request.POST.get('sub')
        email=request.POST.get('email')
        Evaluation.objects.create(fac_name=name,sub=sub,score=score,email=email)
        return redirect('table')
    return render(request,"form.html")