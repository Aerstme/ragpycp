from django.shortcuts import render, redirect


def download(request):
    return render(request, 'download.html', None)

# Create your views here.
