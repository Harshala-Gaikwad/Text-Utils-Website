from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def analyze(request):
    #Get the Text
    djtext = request.POST.get('text','default')

    #Check checkbox value
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps',"off")
    newlineremover = request.POST.get('newlineremover',"off")
    spaceremover = request.POST.get('spaceremover',"off")
    charcount = request.POST.get('charcount',"off")

    #Check which check box is on
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*~'''
        analyzed = ""
        for i in djtext:
            if i not in punctuations:
                analyzed+=i
        params = {'purpose':'Remove Punctuations','analyzed_text':analyzed}
        djtext = analyzed

    if fullcaps=="on":
        analyzed = djtext.upper()
        params = {'purpose':'Captilized Text','analyzed_text':analyzed}
        djtext = analyzed

    if newlineremover=="on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'Remove New Line','analyzed_text':analyzed}
        djtext = analyzed

    if spaceremover == "on":
        # analyzed = djtext.replace(" ","")
        analyzed = ""
        for i,char in enumerate(djtext):
            if djtext[i] == " " and djtext[i+1] == " ":
                pass
            else:
                analyzed += char
        params = {'purpose': 'Remove Space', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == "on":
        djtext = djtext.replace(" ", "")
        analyzed = "No of Character = "+str(len(djtext))
        params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}

    if(removepunc != "on" and newlineremover!="on" and spaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, "analyze.html", params)
