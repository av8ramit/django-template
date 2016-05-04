'''Tests page for the users django template module.'''

from django.test import TestCase
from django.utils import timezone

from .models import ContactRequest

# Create your tests here.
class ContactRequestTests(TestCase):
    '''Tests related to the actual ContactRequest functionality.'''

    def setUp(self):
        self.contact_request = ContactRequest.objects.create_contact_request(
            email="johndoe@email.com",
            text="This is a sample contact request.")

    def test_email_verification(self):
        '''Verify the email.'''
        assert self.contact_request.email == "johndoe@email.com"

    def test_text_verification(self):
        '''Verify the text.'''
        assert self.contact_request.text == "This is a sample contact request."

    def test_bool_properties(self):
        '''Verify that the replied to and resolved are false.'''
        assert not self.contact_request.replied_to
        assert not self.contact_request.resolved

    def test_timestamp(self):
        '''Verify that the request was made before "now".'''
        assert timezone.now() >= self.contact_request.timestamp


