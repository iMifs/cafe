from django.shortcuts import render

def index(request):
    return render(request, 'cafe/index.html')

def menu(request):
    return render(request, 'cafe/menu.html')

def contacts(request):
    return render(request, 'cafe/contacts.html')

def profile(request):
    return render(request, 'accounts/profile.html')