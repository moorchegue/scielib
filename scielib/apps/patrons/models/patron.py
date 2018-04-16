from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Patron(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='patron',
        verbose_name=_("User"),
        on_delete=models.CASCADE,
    )

    class Meta():

        default_related_name = 'patrons'
        verbose_name = _('Patron')
        verbose_name_plural = _('Patrons')

    def __str__(self):
        return '#{}, {}'.format(self.pk, self.user)
