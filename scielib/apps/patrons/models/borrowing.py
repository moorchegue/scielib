from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django_extensions.db.models import TimeStampedModel

from ..exceptions import BorrowingIsAlreadyFinalized


class Borrowing(TimeStampedModel):

    patron = models.ForeignKey(
        "Patron",
        verbose_name=_("Patron"),
        on_delete=models.PROTECT,
    )
    book = models.ForeignKey(
        "books.Book",
        verbose_name=_("Book"),
        on_delete=models.PROTECT,
    )
    borrowed_at = models.DateTimeField(
        verbose_name=_("Borrowed at"), auto_now_add=True)
    got_back_at = models.DateTimeField(
        verbose_name=_("Got back at"), blank=True, null=True)

    def get_back(self):
        if self.got_back_at:
            raise BorrowingIsAlreadyFinalized()

        self.got_back_at = now()
        self.save()
