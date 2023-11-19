from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Folder, Note, User

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect('folders')

    return render(request, 'base/home.html')

def loginPage(request):
    message = ""

    if request.user.is_authenticated:
        return redirect('folders')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('folders')
        else:
            message = "Username or Password is Incorrect!"

    page = 'login'
    context = {'page': page, 'message': message}
    return render(request, 'base/authenticate.html', context)

def signup(request):
    message = ""

    if request.user.is_authenticated:
        return redirect('folders')
    
    if request.method == 'POST':
        full_name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        try:
            user = User.objects.get(username=username)
            if user:
                message = "Uername Already Taken!"
        except:
            if password == confirm_password:
                user = User.objects.create_user(name=full_name, username=username, password=password)
                login(request, user)
                return redirect('folders')
            
            else:
                message = "Password and Confirm Password Doesn't Match!"

    page = 'signup'
    context = {'page': page, 'message': message}
    return render(request, 'base/authenticate.html', context)

@login_required(login_url='login')
def folders(request):   
    if request.method == 'POST':
        folder_name = request.POST.get('folder-name')

        Folder.objects.create(
            user = request.user,
            name = folder_name
        )
    
    q = request.GET.get('q') if request.GET.get('q') != None else '' #SEARCH PARAMETER
    current_user = request.user.id

    all_folders = Folder.objects.filter(
        Q(name__icontains = q) &
        Q(user = current_user)
    )
    context = {'folders': all_folders}
    return render(request, 'base/folders.html', context)


@login_required(login_url='login')
def all_notes(request):
    if request.method == "POST":
        note_heading = request.POST.get('note-heading')
        folder_id = request.POST.get('folder')[0]
        note_body = request.POST.get('note-body')
        note_color = request.POST.get('note-color')

        #NOTES DOESN'T HAVE A FOLDER
        if folder_id == 'N':
            Note.objects.create(
                user = request.user,
                heading = note_heading,
                body = note_body,
                color = note_color
            ).save()

        #NOTES DOES HAVE A FOLDER
        else:
            Note.objects.create(
                user = request.user,
                folder = Folder.objects.get(id=int(folder_id)),
                heading = note_heading,
                body = note_body,
                color = note_color
            ).save()


    q = request.GET.get('q') if request.GET.get('q') != None else '' #SEARCH PARAMETER 
    current_user = request.user.id

    notes = Note.objects.filter(
        Q(Q(heading__icontains = q) |
        Q(body__icontains = q)) &
        Q(user = current_user)
    )

    folders = Folder.objects.filter(
        Q(user=current_user)
    )

    context = {'notes': notes, 'folders': folders}

    return render(request, 'base/notes.html', context)

@login_required(login_url='login')
def notes(request, pk):
    user = request.user

    folders = Folder.objects.filter(
        Q(user=user)
    )
    curr_folder = folders.get(id=int(pk))
    folder_notes = curr_folder.note_set.all()

    context = {'notes': folder_notes, 'folder_name': curr_folder.name, 'folders': folders}

    return render(request, 'base/notes.html', context)

@login_required(login_url='login')
def edit_note(request, pk):
    user = request.user

    note = Note.objects.get(id=int(pk))
    folders = Folder.objects.filter(
        Q(user=user)
    )

    if user != note.user:
        return redirect('all-notes') 

    if request.method == 'POST':
        note.heading = request.POST.get('note-heading')
        note.body = request.POST.get('note-body')
        note.color = request.POST.get('note-color')

        if request.POST.get('folder')[0] != 'N':
            note.folder = Folder.objects.get(id=int(request.POST.get('folder')[0]))

        #WHEN USER CHOOSES TO NOT HAVE FOLDER FOR NOTES
        else:
            note.folder = None

        note.save()

        return redirect('all-notes')

    context = {'note': note, 'folders': folders, 'curr_folder': note.folder}

    return render(request, 'base/edit-note.html', context)

@login_required(login_url='login')
def editProfile(request):
    user = request.user
    message = ""

    if request.method == 'POST':
        full_name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            message = "Username Already Exist!"
        except:
            if username:
                user.username = username

            if full_name:
                user.name = full_name

            if password:
                user.set_password(password)

            user.save()
            return redirect('folders')
        
    context = {'user': user, 'message': message}

    return render(request, 'base/edit-profile.html', context)

@login_required(login_url='login')
def delete_folder(request, pk):
    item = 'folder'
    folder = Folder.objects.get(id=int(pk))

    if request.user != folder.user:
        return redirect('folders')
    
    if request.method == 'POST':
        folder.delete()
        return redirect('folders')

    context = {'item': item, 'folder_name': folder.name}
    return render(request, 'base/delete.html', context)

@login_required(login_url='login')
def delete_note(request, pk):
    item = 'note'
    note = Note.objects.get(id=int(pk))

    if request.user != note.user:
        return redirect('all-notes')    
    
    if request.method == 'POST':
        note.delete()
        return redirect('all-notes')

    context = {'item': item, 'note_name': note.heading}
    return render(request, 'base/delete.html', context)


def delete_account(request):
    user = request.user
    item = 'user'

    if request.method == 'POST':
        user.delete()
        return redirect('home')
    
    context = {'item': item}

    return render(request, 'base/delete.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


