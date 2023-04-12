from django.http import HttpResponse
from django.shortcuts import render

def show_menu(request, name=None):
    return render(request, 'TreeView.html', context={'name': name})
