from django.shortcuts import render , HttpResponse, redirect
# from django.utils.crypto import message 
from models import * 


def index(request):

    return render(request, 'semi_u/index.html', { "users": User.objects.all() })

def new(request):
    return render(request, "semi_u/create.html")

def create(request):
    User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email_add=request.POST['email_add'],
    )
    return redirect('/users')

def edit(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'semi_u/update.html', context)

def update(request, user_id):
    user_to_update = User.objects.get(id=user_id)
    user_to_update.first_name = request.POST['first_name']
    user_to_update.last_name = request.POST['last_name']
    user_to_update.email_add = request.POST['email_add']
    user_to_update.save()
    return redirect('/users')

def show(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'semi_u/show.html', context)


def destroy(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/users')