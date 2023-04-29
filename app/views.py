from django.shortcuts import render

# Create your views here.
def ABCD(request):
    d={'data':'hello thiS is filter Page'}
    return render(request,'ABCD.html',d)

