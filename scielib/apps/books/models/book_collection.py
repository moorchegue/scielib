from django.db import models
from django.utils.translation import ugettext_lazy as _


class BookCollection(models.Model):

    name = models.CharField(
        verbose_name=_("Collection Name"), max_length=64, db_index=True)
    description = models.TextField(verbose_name=_("Collection Description"))

    class Meta():

        default_related_name = 'book_collections'
        verbose_name = _('Book Collection')
        verbose_name_plural = _('Book Collections')
        ordering = ['name']

    def __str__(self):
        return '#{}, {}'.format(self.pk, self.name)
