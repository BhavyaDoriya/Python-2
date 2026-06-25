from django.shortcuts import render,redirect,get_object_or_404
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
def update(request,id):
    fac=get_object_or_404(Evaluation,id=id)
    if request.method=="POST":
        fac.fac_name=request.POST['fac_name']
        fac.sub=request.POST['sub']
        fac.score=request.POST['score']
        fac.email=request.POST['email']
        fac.save()
        return redirect('table')
    return render(request,"update.html",{"fac":fac})
def delete(request,id):
    fac=get_object_or_404(Evaluation,id=id)
    fac.delete()
    return redirect('table')