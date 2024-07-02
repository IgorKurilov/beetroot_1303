from content.models import Category, Note
from datetime import datetime, timedelta

# Створення категорій
category1 = Category.objects.create(title="Personal")
category2 = Category.objects.create(title="Work")

# Створення нотаток
note1 = Note.objects.create(
    title="Buy groceries",
    text="Milk, Bread, Eggs",
    reminder=datetime.now() + timedelta(days=1),
    category=category1
)

note2 = Note.objects.create(
    title="Finish project",
    text="Complete the Django project by the end of the week",
    reminder=datetime.now() + timedelta(days=3),
    category=category2
)

note3 = Note.objects.create(
    title="Call mom",
    text="Call mom to check on her",
    reminder=datetime.now() + timedelta(hours=5),
    category=category1
)
