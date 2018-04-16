from django.db import models
from django.utils.translation import ugettext_lazy as _


class BookGenre(models.Model):

    name = models.CharField(
        verbose_name=_("Genre Name"), max_length=64, db_index=True)
    description = models.TextField(verbose_name=_("Genre Description"))

    class Meta():

        default_related_name = 'book_genres'
        verbose_name = _('Book Genre')
        verbose_name_plural = _('Book Genres')
        ordering = ['name']

    def __str__(self):
        return '#{}, {}'.format(self.pk, self.name)
