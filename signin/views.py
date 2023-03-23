from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import signin

def signup(request):
    if request.method == "POST":
        form = request.POST
        name = form['name']
        password = form['password']
        email = form['email']
        data = signin(name= name, password = password, email = email )
        
        alldata = signin.objects.values()
        for x in range(len(alldata)):
            getdata = signin.objects.values()[x]['email']
            if email == getdata:
                return render(request, 'signupform.html')
        
        data.save()
        res = redirect('/auth')
        return res
        
    else:
        return render(request, 'signupform.html')
    
def login(request):
    
    if request.method == "POST":
        form = request.POST
        email = form['email']
        password = form['password']
        
        alldata = signin.objects.values()
        
        for x in range(len(alldata)):
            
            getdata = signin.objects.values()[x]['email']
            if email == getdata:
                print("email same")
                getpass = signin.objects.values()[x]['password']
                if password == getpass:
                    print("same")
                    return render(request, 'homepage.html')
                else:
                    print("not same")
                    return render(request, 'loginform.html')
        return render(request, 'loginform.html')
                
    else:
        return render(request, 'loginform.html')
    
def showdata(request):
    data = signin.objects.all()
    return HttpResponse(data)
        