from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']
        title = forms.CharField(max_length=50, required=True, label="Title", widget= forms.TextInput(attrs= {'placeholder':'', 'class':"mycssclass", 'id':'jsID'}))
        author = forms.CharField(max_length=50, required= True, label="Author")
        price = forms.DecimalField(required=True, label="Price", initial=0)
        edition = forms.IntegerField(required=True, initial=10, widget=forms.NumberInput())