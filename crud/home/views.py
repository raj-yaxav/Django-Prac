# card/views.py
from django.shortcuts import render, redirect
from .models import Card
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Card.objects.all().delete()
# User.objects.all().delete()

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if User.objects.filter(username =username).exists():
           messages.error(request , "Username already exists")
           return redirect('signup')

        User.objects.create_user(
            username = username,
            password = password
        )

        messages.success(request , "user successfulyy registered")
        return redirect('login')
    return render(request , "home/signup.html")
    
def login_view(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request , username = username , password = password)
        print(user)
        if user is not None:
            login(request , user)
            return redirect('home')
        else : 
            # print("hello")
            messages.error(request , 'Invalid credentials')
            return redirect('login')
    return render(request , "home/login.html") 

# READ

def home(request):
    if request.user.is_authenticated:

     query = request.GET.get("q")
     cards = Card.objects.filter(user = request.user)
    
     
     if query :
        cards = cards.filter(Q(title__icontains=query) | Q(description__icontains = query))
        print(cards)
     return render(request, 'home/home.html', {'cards': cards})
    else :
        messages.error(request, "please login first")
        return redirect("login")
# CREATE
def createCard(request):
    if request.method == "POST":
        Card.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            img=request.POST.get('img'),
            user = request.user
        )
        return redirect('home')

    return render(request, 'home/create.html')

# UPDATE
def updateCard(request, id):
    card = Card.objects.get(id=id)
    if request.method == "POST":
        card.title = request.POST.get('title')
        card.description = request.POST.get('description')
        card.img = request.POST.get('img')
        card.save()
        return redirect('home')
    
    return render(request, 'home/update.html', {'card': card})

# DELETE
def deleteCard(request, id):
    card = Card.objects.get(id=id)
    card.delete()
    return redirect('home')


def logout_view(request):
    logout(request)
    return redirect("login")