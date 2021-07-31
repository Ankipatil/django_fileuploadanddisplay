from django.shortcuts import render,redirect
from . forms import companyform
from . models import company
# Create your views here.

def Home(request):
    if request.method == "POST":
        form = companyform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(read)

    else:
        form = companyform(request.FILES)
    return render(request,"index.html",{"form":form})

def read(request):
    read = company.objects.all()
    return render(request,"read.html",{"read":read})

