from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', {'hithere' : 'This is me !'})
def eggs(request):
    return HttpResponse('Eggs are Great!')
def count(request):
    fulltext = request.GET['fulltext']
    wordcount = fulltext.split()
    worddictonary = {}
    for word in wordcount:
        if word in worddictonary:
            # increase the count
            worddictonary[word] += 1
        else:
            #Adding that into worddictonary
            worddictonary[word] = 1
    sortedwordcount = sorted(worddictonary.items(), key=operator.itemgetter(1), reverse=True)


    return render(request, 'count.html', {'fulltext' : fulltext, 'wordcount': len(wordcount), 'sortedwordcount': sortedwordcount})
    
def about(request):
    return render(request, 'about.html')
