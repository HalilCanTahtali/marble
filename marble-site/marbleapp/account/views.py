
from telnetlib import LOGOUT
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
def login_register_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    if 'giris' in request.POST:
        if request.method == "POST":
            username = request.POST["username"]
            password= request.POST["password"]
            
            user = authenticate(request,username = username, password = password)
            
            if user is not None:
                login(request,user)
                return redirect("home")
            else:
                return render(request,"account/login_register.html",{
                    "error":"Kullanıcı adı veya parola yanlış",
                    "classkaydol": "containerlogin",
                })
    elif 'kaydol' in request.POST:
        if request.method == "POST":
            username= request.POST["username"]
            firstname= request.POST["firstname"]
            lastname= request.POST["lastname"]
            email= request.POST["email"]
            password= request.POST["password"]
            repassword= request.POST["repassword"]
            
            if password == repassword:
                if User.objects.filter(username=username).exists():
                    return render(request,"account/login_register.html",
                        {
                        "error":"Bu kullanıcı adı daha önceden alınmış.",
                        "username":username,
                        "email":email,
                        "firstname":firstname,
                        "lastname":lastname,
                        
                        })
                else:
                    if User.objects.filter(email=email).exists():
                        return render(request,"account/login_register.html",
                        {
                        "error":"Bu mail adresi daha önceden alınmış.",
                        "username":username,
                        "email":email,
                        "firstname":firstname,
                        "lastname":lastname,
                        
                        })
                        
                    else:
                        user = User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname,password=password)    
                        user.save()
                        return redirect("login_register")              
            else:
                return render(request,"account/login_register.html",
                        {
                        "error":"Hatalı parola tekrarı",
                        "username":username,
                        "email":email,
                        "firstname":firstname,
                        "lastname":lastname,
                        
                        })
            
    
    return render(request,"account/login_register.html")

def logout_request(request):
    logout(request)
    return redirect("home")