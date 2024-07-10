# views.py
from django.shortcuts import render
from .models import Note

def home(request):
    notes = Note.objects.all()
    return render(request, 'content/home.html', {'notes': notes})