from django.db import models
from .models import *


def createNewNotes(title: str, content: str):
    newNote = Note.object.create(title=title, content=content)
    newNote.save()