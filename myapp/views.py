from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html") 



def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'default')
    fullcaps = request.POST.get('fullcaps', 'default')
    newlinerem = request.POST.get('newlinerem', 'default')
    extraspacerem = request.POST.get('extraspacerem', 'default')
    charcounter = request.POST.get('charcounter', 'default')
    numberremover = request.POST.get('numberremover', 'default')
    lowchar = request.POST.get('lowchar', 'default')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)


    if(extraspacerem=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (newlinerem == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if (numberremover == "on"):
        analyzed = ""
        numbers = '0123456789'

        for char in djtext:
            if char not in numbers:
                analyzed = analyzed + char
        
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (charcounter=="on"):
        analyzed= ""
        analyzed = analyzed + str(len(djtext.replace(" ","")))
        params = {'purpose': 'Total Number of characters in text', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    

    if(removepunc != "on" and newlinerem!="on" and extraspacerem!="on" and fullcaps!="on" and numberremover != "on" and charcounter!="on"):
        return HttpResponse("please select any operation and try again")
    
    return render(request, 'analyze.html', params)

def about(request):
    return render(request,"about.html") 

def contact(request):
    return render(request,"contact.html") 

    

        
   
# def capfirst(request):
#     return HttpResponse("Capitalize First Letter")

# def newlinerem(request):
#     return HttpResponse("New line remove")

# def spaceremove(request):
#     return HttpResponse("space remover")

# def charcount(request):
#     return HttpResponse("char counter")