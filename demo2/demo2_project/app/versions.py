from django.shortcuts import render, HttpResponse
import requests
import json

def get_app_version():
  
    jsonList = []
    y = requests.get('https://dl.pstmn.io/api/version/latest?platform=osx&channel=stable')
    jsonList.append(json.loads(y.content))
    parsedData = []
    userData = {}
    for data in jsonList:
        userData['version'] = data['version']

    parsedData.append(userData)
    return parsedData
        # return render(request, 'app/test4C.html', {'data': parsedData})




def get_canary_version():
  
    jsonList = []
    y = requests.get('https://dl.pstmn.io/api/version/latest?platform=osx&channel=canary')
    jsonList.append(json.loads(y.content))
    parsedData = []
    userData = {}
    for data in jsonList:
        userData['version'] = data['version']

    parsedData.append(userData)
    return parsedData




def get_version_info():
    jsonList = []
    y = requests.get('https://dl.pstmn.io/changelog?channel=stable&platform=osx')
    jsonList.append(json.loads(y.content))
    parsedData = []
    userData = {}
    for data in jsonList:
        userData['info'] = data['changelog']

    parsedData.append(userData)
    return parsedData


