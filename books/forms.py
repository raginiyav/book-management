from django import forms
from .models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "price",
            "category",
            "published_year",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter book title"}
            ),

            "author": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter author name"}
            ),

            "price": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Enter price"}
            ),

            "category": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter category"}
            ),

            "published_year": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Enter published year"}
            ),
        }