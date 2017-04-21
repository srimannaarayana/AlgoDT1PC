

from django.shortcuts import render
from datetime import datetime
from django.conf import settings
import logging
import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from pip._vendor import requests
import json

def Login(request):   
    return render(request, "index.html")

def ServerTime(request):   
    return HttpResponse(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),status=200);#

def GetAlerts(requests):
     buyData =  [
                       { 'id': '1', 'symbol': 'UVXY', 'action': 'Buy', 'quantity': '100', 'limitprice': '20.00', 'duration': 'now', 'alertedat' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") }

                    
                    ];
     return HttpResponse(json.dumps(buyData) , status=200, content_type='application/json');#
 
class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        