from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from gestion_admin.models import *

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from .decorators import *
# Create your views here.

@yes_connect
def mylogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, 
                            username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.all()[0].name == "admin":
                return redirect('profile')
            elif user.groups.all()[0].name == "user":
                return redirect('home')
    return render(request,'login.html')


@yes_connect
def myregister(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmation = request.POST['Confirmation_password']
        user = User.objects.create_user(username=username, password=password)
        profile = Profile.objects.create(user=user)
        user.groups.add(Group.objects.get(name="user"))
        user.save()
        profile.save()
        return redirect('login')
    return render(request,'register.html')


@login_required(login_url='login')
def mylogout(request):
    logout(request)
    return redirect('login')


def forgot(request):
    return render(request,'forgot.html')


@for_user
def home(request):
    categories = Categorie.objects.all()
    total = {
        'Total Articles': Article.objects.all().count(),
        'Total Catégories': categories.count(),
        'Total Users': User.objects.filter(groups = Group.objects.get(name="user")).count()
    }
    context = {
        'total': total,
        'categories': categories,
    }
    return render(request,'home.html', context)

def categorie(request,id,n):
    data = Article.objects.filter(categorie=id)
    if len(data) <= 5:
        myarticles = data
        context = {
            'articles' : myarticles,
            'n_t' : data.count(),
        }
    else:
        try:
            myarticles = data[n*5:(n+1)*5]
        except IndexError:
            myarticles = data[n*5:]

        if not (data.count() % 5):
            p = list(range(int(data.count()/5)))
        else:
            p = list(range(int(data.count()/5 + 1)))
        pos = int(myarticles[0].id/5)
    
        if n==0:
            n_p = 0
        else:
            n_p = n-1

        if n==p[-1]:
            n_n = n
        else:
            n_n = n+1
        context = {
            'articles' : myarticles,
            'n_t' : data.count(), 'p' : p, 'n' : n, 'n_p' : n_p, 'n_n' : n_n, 'pos' : pos
        }
    return render(request,'categorie.html', context)

@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        f_name, l_name = request.POST['first_name'], request.POST['last_name']
        e, n = request.POST['email'], request.POST['niveau']
        #i = request.FILES['image']
        myprofile = Profile.objects.get(user=request.user)
        myprofile.first_name, myprofile.last_name = f_name, l_name
        myprofile.email, myprofile.niveau = e, Niveau.objects.get(name=n)
        # = i
        if 'image' in request.FILES:
            myprofile.image = request.FILES['image']
        myprofile.save()
        return redirect('profile')

    context = {
        'niveau' : Niveau.objects.all()
    }
    return render(request,'profile.html',context)



@login_required(login_url='login')
def article(request,id):
    myarticle = Article.objects.get(id=id)
    file = myarticle.file.read()

    if request.user.groups.all()[0].name == 'user':
        myhistorique = Historique(user=request.user, article=myarticle)
        myhistorique.save()

    context = {
        'article' : myarticle,
        'file':file.decode("utf-8"),
        'room_name': str(id),
    }
    return render(request,'article.html', context)