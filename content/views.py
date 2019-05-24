from django.shortcuts import render, redirect

#ADD LOGIC AND ACTIONS TO YOUR CUSTOM PAGES HERE

def download(request):
    return render(request, 'download.html', None)

# Create your views here.
