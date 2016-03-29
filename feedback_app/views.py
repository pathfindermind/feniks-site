#! coding: utf-8
from django.conf import settings
from django.views.generic import CreateView
from django.core.mail import send_mail
#
from feedback_app.models import Contact, ContactForm
#
#
class ContactCreateView(CreateView):
    form_class = ContactForm
    template_name = 'feedback_app/contacts.html'
    success_url = '/thanks/'
#
    def form_valid(self, form):
        message = '{name} / {phone} написал: '.format(
            name=form.cleaned_data.get('name').encode('utf-8'),
            phone=form.cleaned_data.get('phone').encode('utf-8')
        )
        message += "\n\n{0}".format(form.cleaned_data.get('text').encode('utf-8'))
        send_mail(
            subject=form.cleaned_data.get('title').encode('utf-8').strip(),
            message=message,
            from_email='contact-form@myapp.com',
            recipient_list=settings.LIST_OF_EMAIL_RECIPIENTS
        )
        return super(ContactCreateView, self).form_valid(form)
