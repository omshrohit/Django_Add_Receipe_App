from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    return redirect('/receipes/')

def  receipes(request):
    if request.method=="POST":
        
        receipe_name=request.POST.get('receipe_name')
        receipe_description=request.POST.get('receipe_description')
        receipe_image=request.FILES.get('receipe_image')
       
        
        print(f"{receipe_name}")
        print(f"{receipe_description}")
       
        print(f"{receipe_image}")
        datas={'receipe_name':receipe_name,'receipe_description':receipe_description,'receipe_image':receipe_image}

        # save  the data
        Receipe.objects.create(
                 receipe_name= receipe_name,
                 receipe_description=receipe_description,
                 receipe_image=receipe_image
        )
        
        # return render(request,'receipes.html',context={'datas':datas})
        return redirect('/receipes/')
    queryset=Receipe.objects.all()
    context={'receipes':queryset}
    return render(request,'receipes.html',context)

def update_receipe(request,id):
    queryset=Receipe.objects.get(id=id)
    if request.method=="POST":

        receipe_name=request.POST.get('receipe_name')
        receipe_description=request.POST.get('receipe_description')
        receipe_image=request.FILES.get('receipe_image')
       
        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description
        if receipe_image:
            queryset.receipe_image=receipe_image

        queryset.save()

        return redirect('/receipes/')

    # if  request.GET.get('search'):
    #     print(request.GET.get('search'))
    #     queryset=queryset.filter(receipe_name__icontains=request.GET.get('search'))

    context={'receipe':queryset}
    return render(request,'update_receipe.html',context)

def delete_receipe(request,id):
    print(id)
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    # return HttpResponse("a")

    return redirect('/receipes/')