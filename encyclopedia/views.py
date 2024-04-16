from django.shortcuts import render

from . import util
import pprint


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def createEntry(request):
    return render(request,"encyclopedia/create.html")

def getEntry(request,title):
    return render(request,"encyclopedia/disply.html",{
        'data':util.get_entry(title),'title': title
    })
