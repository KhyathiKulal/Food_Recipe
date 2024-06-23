from django.shortcuts import render, redirect
from .models import Recipe


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
