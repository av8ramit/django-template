'''Models page for the contact django template module.'''

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ContactRequestManager(models.Manager):
    '''Model manager for the ContactRequest class.'''

    def create_contact_request(self, email, text):
        '''Create a contact request from the email and text information.'''

        contact_request = self.model(
            email=email,
            text=text,
            )
        contact_request.save(using=self._db)
        return contact_request


class ContactRequest(models.Model):
    '''Base model for a Contact form for the website.'''

    email = models.EmailField(max_length=255)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    text = models.TextField()
    replied_to = models.BooleanField(default=False)
    resolved = models.BooleanField(default=False)

    objects = ContactRequestManager()

    class Meta:
        '''Meta class invocation for ContactRequest.'''
        ordering = ['-timestamp']

    def __unicode__(self):
        '''String representation for ContactRequest.'''
        return self.text
