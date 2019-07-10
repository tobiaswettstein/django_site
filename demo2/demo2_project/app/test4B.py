from django.shortcuts import render, HttpResponse
import requests
import json

def add_fours():
    
    # d = 0
    # for i in range (4):
    #     d = d + 4

    # return d

    # x = requests.get('http://dnd5eapi.co/api/monsters/3')
    # content_x = x.text
    # return content_x
        
    parsedData = []
    x = requests.get('http://dnd5eapi.co/api/monsters/3')
    jsonList = []
    jsonList.append(json.loads(x.content))
    userData = {}
    for data in jsonList:
        userData['alignment'] = data['alignment']
        userData['armor_class'] = data['armor_class']
        userData['size'] = data['size']

    parsedData.append(userData)
    return parsedData 
    # return render(request, 'app/test4C.html', {'data': parsedData})


 


def testin():
    # t = 'testing.......'
    # return t
    jsonList = []
    y = requests.get('https://api.github.com/users/tobiaswettstein')
    jsonList.append(json.loads(y.content))
    parsedData = []
    userData = {}
    for data in jsonList:
        userData['name'] = data['name']
        userData['blog'] = data['blog']
        userData['email'] = data['email']
        userData['public_gists'] = data['public_gists']

    parsedData.append(userData)
    return parsedData
    # return render(request, 'app/test4C.html', {'data': parsedData})




    



