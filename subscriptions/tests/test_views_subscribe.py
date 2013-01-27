# coding:utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse

class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('subscriptions:subscribe'))

    def test_get(self):
        """
        GET /inscricao/ must return status code 200.
        """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """
        Response should be a rendered template.
        """
        self.assertTemplateUsed(self.resp,
            'subscriptions/subscription_form.html')

    def test_html(self):
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 4)
        self.assertContains(self.resp, 'type="submit"')


class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name='Henrique Bastos', cpf='12345678901',
            email='henrique@bastos.net', phone='21-96186180')
        url = reverse('subscriptions:subscribe')
        self.resp = self.client.post(url, data)

    def test_post(self):
        """
        Valid POST should redirect to /inscricao/1/
        """
        self.assertEqual(302, self.resp.status_code)

    def test_save(self):
        """
        VALID post must be saved.
        """
        from subscriptions.models import Subscription

        self.assertTrue(Subscription.objects.exists())

class SubscribeInvalidPostTest(TestCase):
    def setUp(self):
        data = dict(name='Henrique Bastos', cpf='12345678210983192083012901',
            email='henrique@bastos.net', phone='21-96186180')
        self.resp = self.client.post(reverse('subscriptions:subscribe'), data)

    def test_post(self):
        """
        Invalid POST should not redirect.
        """
        self.assertEqual(200, self.resp.status_code)

    def test_form_errors(self):
        """
        Form must contain errors
        """
        self.assertTrue(self.resp.context['form'].errors)

    def test_dont_save(self):
        """
        Do not save data.
        """
        from subscriptions.models import Subscription

        self.assertFalse(Subscription.objects.exists())






