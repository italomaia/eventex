# coding:utf-8

from django.test import TestCase

class SubscriptionTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(name='Henrique Bastos', cpf='12345678901',
            email='henrique@bastos.net', phone='21-96186180')
        self.resp = self.client.get(s.get_absolute_url())

    def test_get(self):
        """
        GET /inscricao/1/ should return status 200.
        """
        self.assertEqual(200, self.resp.status_code)

    def test_template_used(self):
        """
        Uses template
        """
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        """
        Context must have a subscription instance.
        """
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        self.assertContains(self.resp, 'Henrique Bastos')

class SubscriptionNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get('/inscricao/0/')
        self.assertEqual(404, response.status_code)