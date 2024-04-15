from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.hashers import make_password
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse




from .models import *
# Create your views here.



from django.shortcuts import render



# Shared Views
def login_form(request):
	return render(request, 'connexion/login.html')



from django.contrib import messages

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            if user.is_admin or user.is_superuser:
                return HttpResponseRedirect(reverse('client'))
            else:
                return HttpResponseRedirect(reverse('client'))
        else:
            # Afficher un message d'erreur si le nom d'utilisateur ou le mot de passe est incorrect
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
            return HttpResponseRedirect(reverse('login'))  # Rediriger vers la page de connexion
    else:
        # Gérer le cas où la méthode HTTP n'est pas POST
        return HttpResponseRedirect(reverse('home'))

			

def logoutView(request):
	logout(request)
	return redirect('home')


def register_form(request):
	return render(request, 'connexion/signup.html')


def registerView(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # Vérifier si un utilisateur avec le même nom d'utilisateur existe déjà
        if User.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur existe déjà.")
            return redirect('register')
        
        # Vérifier si un utilisateur avec la même adresse e-mail existe déjà
        if User.objects.filter(email=email).exists():
            messages.error(request, "Cette adresse e-mail est déjà utilisée.")
            return redirect('register')

        # Hasher le mot de passe
        password_hashed = make_password(password)

        # Créer un nouvel utilisateur
        user = User(username=username, email=email, password=password_hashed)
        user.save()

        messages.success(request, 'Compte bien créé')
        return redirect('home')
    else:
        messages.error(request, 'ERROR')
        return redirect('home')





# Dashboard views

def client(request):
	return render(request, 'dashboard/index.html')