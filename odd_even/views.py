from django.shortcuts import render
from .forms import mahajan


def aman(request):
    fm = mahajan()
    ans="null"
    if request.method=="POST":
        n1=int(request.POST.get("num1"))

        if n1%2==0:
            ans="even"
        else:
            ans="odd"
        
   
    
    return render(request, "index.html", {"forms": fm, "result": ans})
