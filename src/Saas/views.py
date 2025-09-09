from django.shortcuts import render
from visits.models import Visit

def home_page_view(request):
    qs=Visit.objects.all()
    page_qs=Visit.objects.filter(path=request.path)
    context={'title':'Django','total_visits':qs.count()}
    path=request.path
    Visit.objects.create(path=request.path)
    return render (request,'index.html',context)