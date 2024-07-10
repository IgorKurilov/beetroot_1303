# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm
from django.db.models import Q
from datetime import datetime

def note_list(request):
    query = request.GET.get("q")
    category = request.GET.get("category")
    reminder_after = request.GET.get("reminder_after")
    
    notes = Note.objects.all()
    
    if query:
        notes = notes.filter(title__icontains=query)
        
    if category:
        notes = notes.filter(category=category)
        
    if reminder_after:
        try:
            reminder_after_date = datetime.strptime(reminder_after, "%Y-%m-%d %H:%M")
            notes = notes.filter(reminder__gte=reminder_after_date)
        except ValueError:
            pass

    return render(request, 'notes/note_list.html', {'notes': notes})

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    
    return render(request, 'notes/note_detail.html', {'form': form, 'note': note})

def note_new(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm()
    
    return render(request, 'notes/note_edit.html', {'form': form})

def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    
    return render(request, 'notes/note_edit.html', {'form': form})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    
    if request.method == "POST":
        note.delete()
        return redirect('note_list')
    
    return render(request, 'notes/note_delete.html', {'note': note})
