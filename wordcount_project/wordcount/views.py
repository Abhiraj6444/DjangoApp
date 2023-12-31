from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', { 'messageonpage' : "This my first webpage with you" })

def count(request):
    fulltext = request.GET['fulltext']
    worldlist = fulltext.split()
    worddict = dict()
    for word in worldlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
    
    sortedword = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', { 'fulltext' : fulltext, 'count':len(worldlist), 'worddict': sortedword })

def about(request):
    return render(request, 'about.html')