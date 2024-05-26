from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    context={}
    user = request.user.username
    context['user']=user
    return render(request,'index.html',context)

def user_login(request):
    context ={}
    if(request.method=='GET'):
        return render(request,'login.html')
    else:
        uname = request.POST['username']
        upass = request.POST['password']
        if uname=="" or upass=="":
            context['message']="please fill all the fields"
        else:
            u = authenticate(username=uname,password=upass)
            if u is not None:
                login(request,u)
                return redirect('home')
            else:
                context['message']='Invalid Credentials'
        return render(request,'login.html',context)

def user_signup(request):
    context={}
    if(request.method=="GET"):
        return render(request,'signup.html')
    else:
        uname = request.POST['username']
        upass = request.POST['password']
        ucpass = request.POST['confirm_password']
        if uname=="" or upass=="" or ucpass=="":
            context["message"]="please fill all the fileds"
        elif upass!=ucpass:
            context["message"]="password & confirm password must be same"
        else:
            user_object =User.objects.create(password=upass, username=uname, email=uname)
            user_object.set_password(upass)
            user_object.save()
            context["message"]="User registration succesfully"
            return redirect('/')
        return render(request,'signup.html',context)

def user_logout(request):
    logout(request)
    return redirect('/')
    
@login_required
def resume1(request):
    return render(request,'resume1.html')

@login_required
def resume2(request):
    return render(request,'resume2.html')

@login_required
def resume3(request):
    return render(request,'resume3.html')

@login_required
def resume4(request):
    return render(request,'resume4.html')

@login_required
def resume5(request):
    return render(request,'resume5.html')

@login_required
def resume6(request):
    return render(request,'resume6.html')

@login_required
def resume7(request):
    return render(request,'resume7.html')

@login_required
def resume8(request):
    return render(request,'resume8.html')

@login_required
def resume9(request):
    return render(request,'resume9.html')

@login_required
def resume10(request):
    return render(request,'resume10.html')

@login_required
def resume11(request):
    return render(request,'resume11.html')

@login_required
def resume12(request):
    return render(request,'resume12.html')

@login_required
def resume13(request):
    return render(request,'resume13.html')

@login_required
def resume14(request):
    return render(request,'resume14.html')

@login_required
def resume15(request):
    return render(request,'resume15.html')
