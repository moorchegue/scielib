from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel

from scielib.apps.patrons.models.borrowing import Borrowing

from ..exceptions import BookIsNotAvailable, BookIsAlreadyBorrowedByPatron


class Book(TimeStampedModel):

    category = models.ForeignKey(
        'BookCategory',
        verbose_name=_("Book Category"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    genres = models.ManyToManyField(
        'BookGenre', verbose_name=_("Genres"), blank=True)
    collections = models.ManyToManyField(
        'BookCollection', verbose_name=_("Collections"), blank=True)
    authors = models.ManyToManyField('BookAuthor', verbose_name=_("Authors"))
    cover = models.ImageField(
        verbose_name=_("Cover image"),
        upload_to='books/covers',
        blank=True,
        null=True,
    )
    name = models.CharField(
        verbose_name=_("Name"), max_length=255, db_index=True)
    isbn = models.CharField(
        verbose_name=_("ISBN"), max_length=32, db_index=True)
    edition = models.CharField(
        verbose_name=_("Edition"), max_length=64, blank=True, null=True)
    published_at = models.DateTimeField(
        verbose_name=_("Published at"), blank=True, null=True)
    stock = models.IntegerField(verbose_name=_("Stock"), default=1)
    borrowing_price = models.DecimalField(
        verbose_name=_("Borrowing price"), decimal_places=2, max_digits=10)

    class Meta():

        default_related_name = 'books'
        verbose_name = _('Book')
        verbose_name_plural = _('Books')
        ordering = ['name']

    def __str__(self):
        return '#{}, {}'.format(self.pk, self.name)

    @property
    def is_available(self):
        return self.stock > 0

    def borrow_to(self, patron):
        if not self.is_available:
            raise BookIsNotAvailable()

        if Borrowing.objects.filter(
                book=self, patron=patron, got_back_at__isnull=True).exists():
            raise BookIsAlreadyBorrowedByPatron()

        Borrowing.objects.create(book=self, patron=patron)

        self.stock -= 1
        self.save()

    def get_back(self, patron):
        borrowing = Borrowing.objects.get(
            book=self, patron=patron, got_back_at__isnull=True)
        borrowing.get_back()

        self.stock += 1
        self.save()
