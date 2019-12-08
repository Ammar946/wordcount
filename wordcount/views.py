from django.http import response
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    text = request.GET['fulltext']
    words = text.split()
    worddic = {}
    for word in words:
        if word in worddic:
            worddic[word] += 1
        else:
            worddic[word] = 1
    sortedWords = sorted(worddic.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': text, 'count': len(words), 'worddic': sortedWords})