from django.shortcuts import render

def base(request):
    #return HttpResponse('basepage')
    return render(request,'base.html')