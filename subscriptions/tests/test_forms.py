# coding:utf-8

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_csrf(self):
        """
        Html must contain csrf token.
        """
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_form_has_fields(self):
        form = self.resp.context['form']
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)

    def test_cpf_is_digit(self):
        form = self.make_validated_form(cpf='ABCD5678901')

        self.assertItemsEqual(['cpf'], form.errors)

    def test_cpf_has_11_digits(self):
        'CPF must have 11 digits.'
        form = self.make_validated_form(cpf='1234')

        self.assertItemsEqual(['cpf'], form.errors)

    def make_validated_form(self, **kw):
        data = dict(name='Henrique Bastos', email='henrique@bastos.net',
            cpf='12345678901', phone_0='21', phone_1='96186180')
        data.update(kw)
        form = SubscriptionForm(data)
        form.is_valid()
        return form

    def test_email_is_optional(self):
        """Email is optional"""
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_name_must_be_capitalized(self):
        """Name must be capitalized."""
        form = self.make_validated_form(name='HENRIQUE bastos')
        self.assertEqual('Henrique Bastos', form.cleaned_data['name'])

    def test_must_inform_email_or_phone(self):
        """Email and Phone are optional, but one must be informed."""
        form = self.make_validated_form(email='', phone_0='', phone_1='')
        self.assertItemsEqual(['__all__'], form.errors)




