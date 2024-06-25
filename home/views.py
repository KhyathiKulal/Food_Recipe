from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
    if request.method == "POST":
        # recipe_name = request.POST.get('recipe_name')
        data = request.POST
        recipe_name = data.get('recipe_name')
        desc = data.get('desc')
        img = request.FILES.get('img') #for images

        Recipe.objects.create( #creates when u enter
            recipe_name = recipe_name,
            desc = desc,
            img = img
        )
        return redirect('/')

    queryset = Recipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))

    context = {'recipies' : queryset}
    return render(request, 'recipy.html', context)


#delete function
def delete(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/')


#update function
def update(request, id):
    queryset = Recipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        desc = data.get('desc')
        img = request.FILES.get('img')

        queryset.recipe_name = recipe_name
        queryset.desc = desc

        if img :
            queryset.img = img

        queryset.save()
        return redirect('/')
    
    context = { #for passing to template
        'recipies' : queryset
    }
    return render(request, 'update.html', context)


#login function
def login_page(request):
    if request.method == "POST":
        username = request.POST.get("userName")
        password = request.POST.get("pw")

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid Username")
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)
        if user is None :
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else :
            login(request, user)
            return redirect('/')


    return render(request, 'login.html')

#logout function 
def logout_page(request):
    logout(request)
    return redirect('/login')

#registeration func
def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("fn")
        last_name = request.POST.get("ln")
        username = request.POST.get("userName")
        password = request.POST.get("pw")

        #exception handing for same user names
        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "UserName already exists")
            return redirect('/register/')

        user = User.objects.create( #user is predefined class
            first_name = first_name, #use same names, predefined in User class
            last_name = last_name,
            username =  username,
        )

        user.set_password(password)
        user.save()
        # messages.info(request, "Account Created Successfully.")

        return redirect('/login/')

    return render(request, 'register.html')