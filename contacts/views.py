from django.shortcuts import render, get_object_or_404
from .models import Contact
from django.http import Http404
from django.core.paginator import Paginator


def index(request):
    contacts = Contact.objects.all()
    paginator = Paginator(contacts, 10)

    page = request.GET.get('p')
    contacts = paginator.get_page(page)

    return render(request, 'contacts/index.html', {
        'contacts': contacts
    })


def open_contact(request, contact_id):
    # contact = Contact.objects.get(id=contact_id)
    contact = get_object_or_404(Contact, id=contact_id)
    return render(request, 'contacts/open_contact.html', {
        'contact': contact
    })
