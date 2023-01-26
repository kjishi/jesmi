from django.http import HttpResponse
from django.shortcuts import render

from . models import place
from . models import person

# Create your views here.
def demo(request):
    obj=place.objects.all()


    return render(request,"index.html",{'result':obj})

    obj1=person.objects.all()
    return render(request,"index.html",{'res':obj1})







    #name="india"
    #return render(request,"home.html",{'obj':name})


#def addition(request):
    #x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #res=x+y
    #a=int(request.GET['num1'])
    #b=int(request.GET['num2'])
    #c=a-b
    #d=int(request.GET['num1'])
    #e=int(request.GET['num2'])
    #f=d*b
    #g=int(request.GET['num1'])
    #h=int(request.GET['num2'])
    #i=g/h
   # return render(request,"result.html",{'result':res,'sub':c,'mul':f,'div':i})


#def about(request):
 #   return HttpResponse("am mohanlal")
#def contact(request):
 #   return render(request,"result.html")
#def details(request):
 #   return HttpResponse("actor")
#def thanks(request):
 #   return render(request,"thanks.html")