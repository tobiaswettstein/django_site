from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def about(request):
    from pages.namer import my_name
    # from pages.namer import user_name
    return render(request, 'about.html', {'name': my_name})

def contact(request):
    return render(request, 'contact.html', {})


def battle(request):
    from pages.goblin_calculator import add_fours
    return render(request, 'battle.html', {'add': add_fours})


def battle(request):
    from pages.goblin_calculator import adding
    return render(request, 'battle.html', {'adding': adding})

def links(request):
    return render(request, 'links.html', {})