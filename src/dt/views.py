'''Views page for the default django template module.'''

from django.shortcuts import render

def home(request):
    '''Return the view to the home page.'''
    context = {}
    return render(request, "home.html", context)
