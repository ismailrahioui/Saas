from django.shortcuts import render
from visits.models import Visit

def home_view(request,*args,**kwargs):
    return about_view(request,*args,**kwargs)

def about_view(request,*args,**kwargs):
    qs=Visit.objects.all()
    page_qs=Visit.objects.filter(path=request.path)
    try:
        precent=(page_qs.count()*100.0)/qs.count()
    except:
        precent=0
    
    context={
        "title":'Django',
        "page_visit_count":page_qs.count(),
        "percent":precent,
        "total_visit_count":qs.count()
        }
    Visit.objects.create(path=request.path)
    return render (request,'index.html',context)