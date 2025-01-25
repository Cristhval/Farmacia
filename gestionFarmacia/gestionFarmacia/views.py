from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Renderiza el template home.html
