'''Views page for the contact django template module.'''

from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import ContactRequest

# Create your views here.
def contact_us(request):
    '''Return the view to the contact us page.'''

    if request.user.is_authenticated():
        #Default to the user's email address
        form = ContactForm(request.POST or None, initial={
            'email' : request.user.email
            })
    else:
        form = ContactForm(request.POST or None)

    if form.is_valid():
        ContactRequest.objects.create_contact_request(
            email=form.cleaned_data.get('email'),
            text=form.cleaned_data.get('text'),
            )
        messages.success(request, "Thank you! Your feedback has been received.")
        return redirect('home')
    return render(request, "contact/contact_us.html", {'form':form})
