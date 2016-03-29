#! coding: utf-8
from django.db import models
from django.forms import ModelForm, Textarea, TextInput
from captcha.fields import CaptchaField
#
#
class Contact(models.Model):
    title = models.CharField('Тема:', max_length=100)
    name = models.CharField('Имя:', max_length=100)
    phone = models.CharField('Номер телефона:', max_length=100)
    text = models.TextField('Сообщение:')
#
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
#
        def __unicode__(self):
            return '%s' % self.title
#
#
class ContactForm(ModelForm):
    captcha = CaptchaField(label='Проверочный код:')
#
    class Meta:
            model = Contact
            exclude = []
            widgets = {
            'text': Textarea(attrs={
            'cols': 80, 'rows': 10, 'id': 'messagestyle','placeholder' : 'Текст'}),
            'name': TextInput(attrs={
            'id': 'namestyle', 'placeholder' : 'Имя'}),
            'title': TextInput(attrs={
            'id': 'subjectstyle','placeholder' : 'Тема сообщения'}),
            'phone': TextInput(attrs={
            'id': 'tellstyle', 'placeholder' : 'Номер телефона'})
            }
