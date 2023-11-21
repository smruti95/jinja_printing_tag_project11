from django.shortcuts import render

# Create your views here.
def login(request):
    d={'username':'smruti'}
    return render(request,'login.html',context=d)