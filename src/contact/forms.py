'''Forms page for the users django template module.'''

from django import forms

from .models import ContactRequest

class ContactForm(forms.ModelForm):
    '''A form for contacting the administrators.'''

    class Meta:
        '''Meta class invocation for ContactRequest.'''
        model = ContactRequest
        fields = [
            "email",
            "text",
            ]
