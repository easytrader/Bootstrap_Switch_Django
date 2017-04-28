from django.shortcuts import render,render_to_response
from django.template import RequestContext
import sys
import os

# Create your views here.
def hello_world(request):
    return render_to_response('hello_world.html',{},context_instance = RequestContext(request))