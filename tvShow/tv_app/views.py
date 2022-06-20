from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render

from tv_app.models import Show

# Create your views here.
def index(request):
    return render(request,"index.html")


def shows(request):
    shows=Show.objects.all()
    context={
       "shows":shows
    }

    return render(request,"shows.html",context)


def create(request):# create show from the form 
    if request.method == "POST": #check for post method 
        title=request.POST.get("title")
        network=request.POST.get("network")
        releseDate=request.POST.get("releseDate")
        desc=request.POST.get("desc")
        #create obj of model
        newShow=Show.objects.create(title=title,network=network,releseDate=releseDate,desc=desc)
        return redirect(f"/show/{newShow.id}")



def showbyid(request,id):
    #fetch the show by id in model

    show=Show.objects.get(id=id)
    context={
        "show":show
    }
    return render(request,'showbyid.html',context)

def edit(request,id):#for edit btn 
    show = Show.objects.get(id=id)

    if request.method == "POST": #check for post method 
      
        #all field have to change    
        #show.title= request.POST.get('title')

        #show.network=request.POST.get('network')

       # show.releseDate=request.POST.get('releseDate') 	

       # show.desc=request.POST.get('desc') 
       # show.save()


        #if one field changed| no need for change the old value
        show.title= request.POST.get('title') if request.POST.get('title')  else show.title

        show.network=request.POST.get('network') if request.POST.get('network') else show.network

        show.releseDate=request.POST.get('releseDate') if request.POST.get('releseDate') else show.releseDate	

        show.desc=request.POST.get('desc') if request.POST.get('desc') else show.desc
        show.save()
        return redirect(f"/show/{show.id}")
    
    
    context={
        "show":show,
    }
    return render(request,'edit.html',context)



def delete(request,id):
    show = Show.objects.get(id=id)
#if (show):
    show.delete()
    return redirect("/shows")









