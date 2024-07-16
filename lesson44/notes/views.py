from django.shortcuts import render

def notes_list(request):
    test_data = [
        {"title": "Note 1", "content": "Content for note 1"},
        {"title": "Note 2", "content": "Content for note 2"},
        {"title": "Note 3", "content": "Content for note 3"},
    ]
    return render(request, 'notes/notes_list.html', {'notes': test_data})
