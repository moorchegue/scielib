from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django_extensions.db.models import TimeStampedModel


class Review(TimeStampedModel):

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
    review_text = models.TextField(verbose_name=_("Review text"))
    review_score = models.PositiveSmallIntegerField(
        verbose_name=_("Review score"),
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ],
    )
