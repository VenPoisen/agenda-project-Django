from django.shortcuts import render
from .models import Contact


def index(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/index.html', {
        'contacts': contacts
    })


def open_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    return render(request, 'contacts/open_contact.html', {
        'contact': contact
    })
