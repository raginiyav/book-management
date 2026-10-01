from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    book_register,
    book_edit,
    book_delete,
    dashboard,
    BookViewSet,
)


router = DefaultRouter()

router.register(
    "api/books",
    BookViewSet,
    basename="book"
)


urlpatterns = [

    # Dashboard
    path(
        "",
        dashboard,
        name="dashboard"
    ),

    # Book Register
    path(
        "register/",
        book_register,
        name="book_register"
    ),

    # Edit
    path(
        "edit/<int:id>/",
        book_edit,
        name="book_edit"
    ),

    # Delete
    path(
        "delete/<int:id>/",
        book_delete,
        name="book_delete"
    ),

    # API
    path(
        "",
        include(router.urls)
    ),

 # REST API
    path(
        "",
        include(router.urls)
    ),

]

