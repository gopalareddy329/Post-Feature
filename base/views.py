from django.shortcuts import render,redirect
from . forms import Userform,Postform
from . models import User,Post
from django.contrib.auth import authenticate,login,logout
def home(request):
    form=Userform()
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            return redirect('home')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        
    context={'forms':form}
    return render(request,'home.html',context)

def logoutuser(request):
    logout(request)
    return redirect('home')


def Post_User(request):
    posts=Post.objects.all()
    
    context={'posts':posts}
    return render(request,'posts.html',context)


def addpost(request):
    form=Postform()
    if request.method=="POST":
        form=Postform(request.POST,request.FILES)
        if form.is_valid():
            form1=form.save(commit=False)
            form1.host=request.user
            form1.save()
            return redirect('home')
    context={'form':form}
    return render(request,'add.html',context)