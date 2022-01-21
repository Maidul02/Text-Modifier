#This file is created manually
import string
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,"index.html")

def analyze(request):
    djtext = request.POST.get("text","default")
    removepunc = request.POST.get("removepunc","off")
    fullcaps = request.POST.get("fullcaps","off")
    newlineremover = request.POST.get("newlineremover","off")
    extraspaceremover = request.POST.get("extraspaceremover","off")
    analyzed = ""
    params = {"purpose":"Nothing", "analyzed_text":analyzed}
    purpose = ""
    
    if removepunc=="on":
        analyzed = ""
        for i in djtext:
            if i not in string.punctuation:
                analyzed+=i
        
        djtext = analyzed
        purpose+=", Removed punctuations"
    
    if fullcaps=="on":
        analyzed = ""
        analyzed = djtext.upper()
        djtext = analyzed
        purpose+=", Made Uppercase"
    
    if newlineremover=="on":
        analyzed = ""
        for i in djtext:
            if i!="\n" and i!="\r":
                analyzed+=i
        djtext = analyzed
        purpose+=", Removed newlines"
    
    if extraspaceremover=="on":
        analyzed = ""
        for i in range(len(djtext)-1):
            if not(djtext[i]==" " and djtext[i+1]==" "):
                analyzed+=djtext[i]
        if djtext[len(djtext)-1]!=" ":
            analyzed+=djtext[len(djtext)-1]
        djtext = analyzed
        purpose+=", Removed extra spaces"
        
    if analyzed=="":
        analyzed = "No text has been analyzed"
    params = {"purpose":purpose, "analyzed_text":analyzed}
    return render(request, "analyze.html", params)




def about(request):
    
    return render(request,"about.html")



























