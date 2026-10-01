from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Sum, Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import BookForm
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework import viewsets
from .serializers import BookSerializer


@login_required
def book_register(request):

    if request.method == "POST":

        form = BookForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Book registered successfully! 📚"
            )

            return redirect("book_register")

    else:

        form = BookForm()


    # Search
    search = request.GET.get("search", "")

    # Category filter
    category = request.GET.get("category", "")


    books = Book.objects.all().order_by("-id")


    # Search by title or author
    if search:

        books = books.filter(
            title__icontains=search
        ) | books.filter(
            author__icontains=search
        )


    # Filter by category
    if category:

        books = books.filter(
            category__iexact=category
        )


    # Categories
    categories = Book.objects.values_list(
        "category",
        flat=True
    ).distinct()


    # Pagination
    paginator = Paginator(
        books,
        5
    )

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(
        page_number
    )


    return render(
        request,
        "books/book_register.html",
        {
            "form": form,
            "books": page_obj,
            "page_obj": page_obj,
            "categories": categories,
            "search": search,
            "selected_category": category,
        },
    )


@login_required
def book_edit(request, id):

    book = get_object_or_404(
        Book,
        id=id
    )


    if request.method == "POST":

        form = BookForm(
            request.POST,
            instance=book
        )


        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Book updated successfully! ✏️"
            )

            return redirect(
                "book_register"
            )


    else:

        form = BookForm(
            instance=book
        )


    books = Book.objects.all().order_by("-id")


    return render(
        request,
        "books/book_register.html",
        {
            "form": form,
            "books": books,
            "edit_mode": True,
            "edit_id": book.id,
        },
    )


@login_required
def book_delete(request, id):

    book = get_object_or_404(
        Book,
        id=id
    )


    if request.method == "POST":

        book.delete()

        messages.success(
            request,
            "Book deleted successfully! 🗑️"
        )

        return redirect(
            "book_register"
        )


    return render(
        request,
        "books/book_delete.html",
        {
            "book": book
        },
    )


@login_required
def dashboard(request):

    total_books = Book.objects.count()


    total_authors = Book.objects.values(
        "author"
    ).distinct().count()


    total_categories = Book.objects.values(
        "category"
    ).distinct().count()


    total_value = Book.objects.aggregate(
        total=Sum("price")
    )["total"] or 0


    recent_books = Book.objects.all().order_by(
        "-id"
    )[:5]


    category_data = Book.objects.values(
        "category"
    ).annotate(
        total=Count("id")
    ).order_by("-total")


    return render(
        request,
        "books/dashboard.html",
        {
            "total_books": total_books,
            "total_authors": total_authors,
            "total_categories": total_categories,
            "total_value": total_value,
            "recent_books": recent_books,
            "category_data": category_data,
        },
    )

class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all().order_by("-id")

    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all().order_by("-id")

    serializer_class = BookSerializer