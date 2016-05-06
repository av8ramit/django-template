'''Views page for the default django template module.'''

from django.shortcuts import render

def home(request):
    '''Return the view to the home page.'''
    context = {}
    if request.user.is_authenticated():
        return render(request, "home_user.html", context)
    else:
        return render(request, "home_visitor.html", context)
