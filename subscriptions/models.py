# coding:utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Subscription(models.Model):
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    name = models.CharField(_('Nome'), max_length=100)
    cpf = models.CharField(_('CPF'), max_length=16, unique=True)
    email = models.EmailField(_('Email'), unique=True)
    phone = models.CharField(_('Telefone'), max_length=20, blank=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = _('inscrição')
        verbose_name_plural = _('inscrições')

    def __unicode__(self):
        return self.name