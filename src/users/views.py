'''Views page for the users django template module.'''

from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import EditProfileForm

# Create your views here.
def edit_profile(request):
    '''Return the view to the edit profile page.'''
    form = EditProfileForm(request.POST or None, request.FILES or None, initial={
        'first_name' : request.user.first_name,
        'last_name' : request.user.last_name,
        'image' : request.user.image})
    if form.is_valid():
        request.user.first_name = form.cleaned_data.get('first_name')
        request.user.last_name = form.cleaned_data.get('last_name')
        request.user.image = form.cleaned_data.get('image')
        request.user.save()
        messages.success(request, "Your profile has been updated.")
        return redirect("edit_profile")
    return render(request, "users/edit_profile.html", {'form':form})
