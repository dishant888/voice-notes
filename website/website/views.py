from django.shortcuts import render, redirect

notesList = [
    {'id':1,'Title':'Title 1','Description':'description 1'},
    {'id':2,'Title': 'Title 2', 'Description': 'description 2'},
    {'id':3,'Title': 'Title 3', 'Description': 'description 3'},
    {'id':4,'Title': 'Title 4', 'Description': 'description 4'},
]

def index(req):
    return render(req,'notes.html')

def saveNote(req):
    title = req.GET.get('title')
    description = req.GET.get('description')
    notesList.append({'id':len(notesList)+1,"Title":title,"Description":description})
    return redirect(notes)

def notes(req):
    return render(req,'notesList.html',context={"notes":notesList})

def deleteNote(req,note_id):
    notesList[:] = [note for note in notesList if note['id'] != note_id]
    return redirect(notes)

def viewNote(req,note_id):
    note = list(filter(lambda note: note['id'] == note_id, notesList))
    print(note)
    return render(req,'viewNote.html',context={"note":note[0]})