from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def aboutus(request):
    return render(request,'aboutus.html')
def packages(request):
    return render(request,'packages.html')

def gallery(request):
    return render(request,'gallery.html')

