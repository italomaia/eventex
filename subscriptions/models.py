# coding:utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Subscription(models.Model):
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    name = models.CharField(_('Nome'), max_length=100)
    cpf = models.CharField(_('CPF'), max_length=16, unique=True)
    email = models.EmailField(_('Email'), blank=True)
    phone = models.CharField(_('Telefone'), max_length=20, blank=True)
    paid = models.BooleanField(_('Pago'), default=False)

    class Meta:
        ordering = ['created_at']
        verbose_name = _(u'inscrição')
        verbose_name_plural = _(u'inscrições')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('subscriptions:subscription', [str(self.id)])