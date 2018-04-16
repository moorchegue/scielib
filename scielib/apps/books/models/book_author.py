from django.db import models
from django.utils.translation import ugettext_lazy as _


class BookAuthor(models.Model):

    name = models.CharField(
        verbose_name=_("Name"), max_length=64, db_index=True)
    bio = models.TextField(verbose_name=_("Author Biography"))

    class Meta():

        default_related_name = 'book_authors'
        verbose_name = _('Book Author')
        verbose_name_plural = _('Book Authors')
        ordering = ['name']

    def __str__(self):
        return '#{}, {}'.format(self.pk, self.name)
