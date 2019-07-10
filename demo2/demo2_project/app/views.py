from django.shortcuts import render, HttpResponse

import requests
import json
from django.template import RequestContext



from .forms import DictionaryForm # needs this for oxford dict page

# def fortress_battle_view(request):
#     from app.epic_battle_math import fortress_battle
#     return render(request, 'app/epic_battle.html', {'fb': fortress_battle})

# def epic_battle(request):
#     from app.epic_battle_math import fortress_battle
#     return render(request, 'app/epic_battle.html', {'fbb': fortress_battle})

def postman_google_analytics(request):
    from app.service_account import get_access_token
    from app.HelloAnalytics import (avg_session_dur, amount_of_sessions)
    return render(request, 'app/google_analytics.html', {'google_a1': avg_session_dur, 'google_a2': amount_of_sessions, 'google_a3': get_access_token})


def show_app_version(request):
    from app.versions import get_app_version, get_canary_version, get_version_info
    return render(request, 'app/versions.html', {'version': get_app_version, 'c_version': get_canary_version, 'info': get_version_info})


def calculator(request):
    from app.calculator import one_one
    return render(request, 'app/calculator.html', {'one': one_one})


def oxford(request):
    search_result = {}
    if 'word' in request.GET:
        form = DictionaryForm(request.GET)
        if form.is_valid():
            search_result = form.search()
    else:
        form = DictionaryForm()
    return render(request, 'app/oxford.html', {'form': form, 'search_result': search_result})


def index(request):
    return HttpResponse('Hello World!!!!!!!!<br/><br/> this is my first view')


def test(request):
    return HttpResponse('My second view!!!!!!!')


def test2(request):
    return HttpResponse('My third view!!!!!!!')

def test4(request):
    from app.test4B import add_fours, testin
    return render(request, 'app/test4A.html', {'add': add_fours, 'test1': testin})

    # x = requests.get('http://dnd5eapi.co/api/monsters/3')
    # content_x = x.text

    # y = requests.get('https://api.github.com/users/tobiaswettstein')
    # content_y = y.text

    # return HttpResponse(content_x + '<br/><br/><br/>' + content_y)







# def profile(request):
#     jsonList = []
#     req = requests.get('https://api.github.com/users/tobiaswettstein')
#     jsonList.append(json.loads(req.content))
#     parsedData = []
#     userData = {}
#     for data in jsonList:
#         userData['name'] = data['name']
#         userData['blog'] = data['blog']
#         userData['email'] = data['email']
#         userData['public_gists'] = data['public_gists']
#         userData['public_repos'] = data['public_repos']
#         userData['avatar_url'] = data['avatar_url']
#         userData['followers'] = data['followers']
#         userData['following'] = data['following']
#     parsedData.append(userData)
#     # return HttpResponse(parsedData)

#     return render(request, 'app/profile.html', {'data': parsedData})

# import json
# from django.shortcuts import *
# from django.template import RequestContext
# from linki.forms import *





import json as simplejson
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
def profile(request):
    userData = {}
    parsedData = []
    if request.method == 'POST':
        
        username = request.POST.get('user')
        req = requests.get('https://api.github.com/users/' + username)
        jsonList = []
        jsonList.append(json.loads(req.content))
        userData = {}
        for data in jsonList:
            userData['name'] = data['name']
            userData['blog'] = data['blog']
            userData['email'] = data['email']
            userData['public_gists'] = data['public_gists']
            userData['public_repos'] = data['public_repos']
            userData['avatar_url'] = data['avatar_url']
            userData['followers'] = data['followers']
            userData['following'] = data['following']
        parsedData.append(userData)

        # User.objects.create(
        #     name = name,
        #     blog = blog,
        #     email = email,
        #     public_gists = public_gists,
        #     public_repos = public_repos,
        #     avatar_url = avator_url,
        #     followers = followers,
        #     following = following,
        # )


    #     return HttpResponse(simplejson.dumps(userData), content_type='application/javascript')
    # return render_to_response('app/profile.html', {'data': userData})


    #     return HttpResponseRedirect("app/profile.html")
    # return render_to_response("normal/template.html", {"form":form}, context_instance=RequestContext(request))

        # return HttpResponse(userData)   
	   
	        
    return render(request,'app/profile.html',{'data': parsedData})

# def dragon(request):
    
#     parsedData = []
#     x = requests.get('http://dnd5eapi.co/api/monsters/3')
#     jsonList = []
#     jsonList.append(json.loads(x.content))
#     userData = {}
#     for data in jsonList:
#         userData['alignment'] = data['alignment']
#         userData['armor_class'] = data['armor_class']
#         userData['size'] = data['size']

#     parsedData.append(userData)
#     # return parsedData
#     return render(request, 'app/test4C.html', {'data': parsedData})

# def github(request):
    
#     parsedData2 = []
#     x2 = requests.get('https://api.github.com/users/tobiaswettstein')
#     jsonList2 = []
#     jsonList2.append(json.loads(x2.content))
#     userData2 = {}
#     for data2 in jsonList2:
#         userData2['name'] = data2['name']
#         userData2['blog'] = data2['blog']
#         userData2['email'] = data2['email']
#         userData2['public_gists'] = data2['public_gists']


#     parsedData2.append(userData2)
#     # return parsedData2
#     return render(request, 'app/test4C.html', {'data2': parsedData2})

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def test5(request):
    pd = [8, 24, 'kb']
    user_data = {}

    if request.method == 'POST':

        x = request.POST.get('x') 

        pd.append(x)

    # return JsonResponse(status = 200, data = {'pd' : pd})
    # return HttpResponse(json.dumps({'pd' : pd}))

    return render(request,'app/test5.html',{'pd': pd})

