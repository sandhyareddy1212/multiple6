from django.shortcuts import render

# Create your views here.
def dk(request):
    dict={'a':10,'b':20}
    return render(request,'dk.html',context=dict)
