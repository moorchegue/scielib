from django.db import models
from django.utils.translation import ugettext_lazy as _


class BookCategory(models.Model):

    name = models.CharField(
        verbose_name=_("Category Name"), max_length=64, db_index=True)
    description = models.TextField(verbose_name=_("Category Description"))

    class Meta():

        default_related_name = 'book_categories'
        verbose_name = _('Book Category')
        verbose_name_plural = _('Book Categories')
        ordering = ['name']

    def __str__(self):
        return '#{}, {}'.format(self.pk, self.name)
