from django.conf.urls import url, include
from rest_framework import routers

from .views import (
    book,
    book_category,
    book_genre,
    book_collection,
    book_author,
)


router = routers.DefaultRouter()
router.register(r'books', book.BookViewSet)
router.register(r'book_categories', book_category.BookCategoryViewSet)
router.register(r'book_genres', book_genre.BookGenreViewSet)
router.register(r'book_collections', book_collection.BookCollectionViewSet)
router.register(r'book_authors', book_author.BookAuthorViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
]
