from django.shortcuts import render

# Create your views here.
def ifb(request):
    d={'a':1,'b':5}
    return render(request,'r.html',d)