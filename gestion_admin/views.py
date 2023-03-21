from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .models import *

from django.contrib.auth.decorators import login_required

from .decorators import *



# Create your views here.


@login_required(login_url='login')
@for_admin
def profiles(request,n):
    data = Profile.objects.all()
    if len(data) <= 10:
        myprofiles = data
        context = {
            'profiles' : myprofiles,
            'n_t' : data.count()
        }
    else:
        try:
            myprofiles = data[n*10:(n+1)*10]
        except IndexError:
            myprofiles = data[n*10:]
        if not (data.count() % 10):
            p = list(range(int(data.count()/10)))
        else:
            p = list(range(int(data.count()/10 + 1)))
        pos = int(myprofiles[0].id/10)
    
        if n==0:
            n_p = 0
        else:
            n_p = n-1

        if n==p[-1]:
            n_n = n
        else:
            n_n = n+1
        context = {
            'profiles' : myprofiles,
            'n_t' : data.count(), 'p' : p, 'n' : n, 'n_p' : n_p, 'n_n' : n_n, 'pos' : pos
        }
    return render(request,'profile/liste_profile.html', context)


@login_required(login_url='login')
@for_admin
def update_profile(request,id):
    myprofile = Profile.objects.get(id=id)
    if request.method == 'POST':
        f_name, l_name = request.POST['first_name'], request.POST['last_name']
        e, n = request.POST['email'], request.POST['niveau']
        r = request.POST['role']

        myprofile.first_name, myprofile.last_name = f_name, l_name
        myprofile.email, myprofile.niveau = e, Niveau.objects.get(name=n)
        if 'image' in request.FILES:
            myprofile.image = request.FILES['image']
        myprofile.user.groups.clear()
        myprofile.user.groups.add(Group.objects.get(name=r))
        myprofile.save()
        return redirect('profile_edit', id=id)
    
    context = {
        'profile' : myprofile,
        'niveau' : Niveau.objects.all(),
        'role': Group.objects.all().values_list('name', flat=True)
    }
    return render(request,'profile/edit_profile.html', context)









@login_required(login_url='login')
@for_admin
def categories(request,n):
    data = Categorie.objects.all()
    if len(data) <= 10:
        mycategories = data
        context = {
            'categories' : mycategories,
            'n_t' : data.count()
        }
    else:
        try:
            mycategories = data[n*10:(n+1)*10]
        except IndexError:
            mycategories = data[n*10:]
        if not (data.count() % 10):
            p = list(range(int(data.count()/10)))
        else:
            p = list(range(int(data.count()/10 + 1)))
        pos = int(mycategories[0].id/10)
    
        if n==0:
            n_p = 0
        else:
            n_p = n-1

        if n==p[-1]:
            n_n = n
        else:
            n_n = n+1
        context = {
            'categories' : mycategories,
            'n_t' : data.count(), 'p' : p, 'n' : n, 'n_p' : n_p, 'n_n' : n_n, 'pos' : pos
        }
    return render(request,'categorie/liste_categorie.html', context)


@login_required(login_url='login')
@for_admin
def update_categorie(request,id):
    mycategorie = Categorie.objects.get(id=id)
    if request.method == 'POST':
        mycategorie.name = request.POST['name']
        mycategorie.save()
        return redirect('categories', n=0)
    context = {
        'categorie' : mycategorie,
    }
    return render(request,'categorie/edit_categorie.html', context)


@login_required(login_url='login')
@for_admin
def create_categorie(request):
    if request.method == 'POST':
        Categorie(name=request.POST['name']).save()
        return redirect('categories', n=0)
    return render(request,'categorie/create_categorie.html')









@login_required(login_url='login')
@for_admin
def niveaux(request, n):
    data = Niveau.objects.all()
    n_t = data
    if len(data) <= 10:
        myniveaux = data
        context = {
            'niveaux' : myniveaux,
            'n_t' : data.count()
        }
    else:
        try:
            myniveaux = data[n*10:(n+1)*10]
        except IndexError:
            myniveaux = data[n*10:]

        print(len(data))
        if not (data.count() % 10):
            p = list(range(int(data.count()/10)))
        else:
            p = list(range(int(data.count()/10 + 1)))
        pos = int(myniveaux[0].id/10)
    
        if n==0:
            n_p = 0
        else:
            n_p = n-1

        if n==p[-1]:
            n_n = n
        else:
            n_n = n+1
        context = {
            'niveaux' : myniveaux, 'n_t' : data.count(), 
            'p' : p, 'n' : n, 'n_p' : n_p, 
            'n_n' : n_n, 'pos' : pos
        }
    return render(request,'niveau/liste_niveau.html', context)



@login_required(login_url='login')
@for_admin
def update_niveau(request,id):
    myniveau = Niveau.objects.get(id=id)
    if request.method == 'POST':
        myniveau.name = request.POST['name']
        myniveau.save()
        return redirect('niveaux', n=0)
    context = {
        'niveau' : myniveau,
    }
    return render(request,'niveau/edit_niveau.html', context)


@login_required(login_url='login')
@for_admin
def create_niveau(request):
    if request.method == 'POST':
        Niveau(name=request.POST['name']).save()
        return redirect('niveaux', n=0)
    return render(request,'niveau/create_niveau.html')











@login_required(login_url='login')
@for_admin
def articles(request, n):
    data = Article.objects.all()
    if len(data) <= 10:
        myarticles = data
        context = {
            'articles' : myarticles,
            'n_t' : data.count()
        }
    else:
        try:
            myarticles = data[n*10:(n+1)*10]
        except IndexError:
            myarticles = data[n*10:]

        if not (data.count() % 10):
            p = list(range(int(data.count()/10)))
        else:
            p = list(range(int(data.count()/10 + 1)))
        pos = int(myarticles[0].id/10)
    
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
    return render(request,'article/liste_article.html', context)

@login_required(login_url='login')
@for_admin
def update_article(request,id):
    myarticle = Article.objects.get(id=id)
    if request.method == 'POST':
        t, c = request.POST['title'], Categorie.objects.get(name=request.POST['categorie'])
        if 'image' in request.FILES and 'file' in request.FILES:
            i, f = request.FILES['image'], request.FILES['file']
            myarticle.description = f.read().decode('utf-8')
            myarticle.image, myarticle.file = i, f
        myarticle.title, myarticle.categorie = t, c
        myarticle.save()
        return redirect('articles', n=0)
    context = {
        'article' : myarticle,
        'categorie' : Categorie.objects.all(),
    }
    return render(request,'article/edit_article.html',context)

def create_article(request):
    if request.method == 'POST':
        d = None
        t, c = request.POST['title'], Categorie.objects.get(name=request.POST['categorie'])
        if 'image' in request.FILES and 'file' in request.FILES:
            i, f = request.FILES['image'], request.FILES['file']
            d = f.read().decode('utf-8')[:400] + ' ...'
            myarticle =Article(title=t, categorie=c, image=i, file=f, description=d)
            myarticle.save()
            return redirect('articles', n=0)
    context = {
        'categorie' : Categorie.objects.all(),
    }
    return render(request,'article/create_article.html', context)













@login_required(login_url='login')
@for_admin
def historique(request, n):
    data = Historique.objects.all()
    if len(data) <= 10:
        myhistoriques = data
        context = {
            'historique' : myhistoriques,
            'n_t' : data.count()
        }
    else:
        try:
            myhistoriques = data[n*10:(n+1)*10]
        except IndexError:
            myhistoriques = data[n*10:]

        if not (data.count() % 10):
            p = list(range(int(data.count()/10)))
        else:
            p = list(range(int(data.count()/10 + 1)))
        pos = int(myhistoriques[0].id/10)
    
        if n==0:
            n_p = 0
        else:
            n_p = n-1

        if n==p[-1]:
            n_n = n
        else:
            n_n = n+1
        context = {
            'historique' : myhistoriques,
            'n_t' : data.count(), 'p' : p, 'n' : n, 'n_p' : n_p, 'n_n' : n_n, 'pos' : pos
        }
    return render(request,'historique.html', context)










