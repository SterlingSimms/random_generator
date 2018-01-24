from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if "number" not in request.session.keys():
        request.session["number"] = 0
    else:
        request.session["number"] = request.session["number"] + 1
    context = {
    "random" : get_random_string(length=14),
    "number" : request.session["number"]
    }
    return render(request, 'random_word/index.html', context)

def reset(request):
    request.session["number"] = 0
    return redirect("/")
