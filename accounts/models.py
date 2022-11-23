from django.db import models
from contacts.models import Contact
from django import forms


class FormContact(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormContact, self).__init__(*args, **kwargs)
        self.fields['creation_date'].widget.attrs['readonly'] = True

    class Meta:
        model = Contact
        exclude = ('show',)
