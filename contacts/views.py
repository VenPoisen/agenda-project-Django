from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models. functions import Concat
from django.contrib import messages


def index(request):
    contacts = Contact.objects.order_by('-id')
    paginator = Paginator(contacts, 20)

    page = request.GET.get('p')
    # contacts = paginator.get_page(page)

    return render(request, 'contacts/index.html', {
        'contacts': contacts
    })


def open_contact(request, contact_id):
    # contact = Contact.objects.get(id=contact_id)
    contact = get_object_or_404(Contact, id=contact_id)

    if not contact.show:
        raise Http404()

    return render(request, 'contacts/open_contact.html', {
        'contact': contact
    })


def search(request):
    term = request.GET.get('term')

    if term is None or not term:
        messages.add_message(
            request,
            messages.ERROR,
            'Search field cannot be empty'
        )
        return redirect('index')

    fields = Concat('name', Value(' '), 'last_name')

    # contacts = Contact.objects.order_by(
    #     '-id').filter(Q(name__icontains=term) | Q(last_name__icontains=term),)
    contacts = Contact.objects.annotate(
        full_name=fields
    ).filter(
        Q(full_name__icontains=term) | Q(
            telephone__icontains=term)
    ).order_by('-id')
    paginator = Paginator(contacts, 10)

    page = request.GET.get('p')
    contacts = paginator.get_page(page)

    return render(request, 'contacts/search.html', {
        'contacts': contacts
    })
