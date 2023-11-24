from django.shortcuts import render
import time

def home(request):
    return render(request, 'home.html', {'name': 'Varun Tiwari'})

def add(request):
    a = int(request.GET['n1'])
    b = int(request.GET['n2'])
    res = a + b
    x=res
    for i in range(res,0,-1):
        time.sleep(2)
        print(x)
        return render(request, "home.html", {'result': x})
    
            
    # return render(request, "home.html", {'result': res})