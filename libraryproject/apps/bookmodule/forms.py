from django import forms
from .models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']
    title = forms.CharField(max_length=50, required=True, label="Title", widget= forms.TextInput(attrs= {'placeholder':'', 'class':"mycssclass", 'id':'jsID'}))
    author = forms.CharField(max_length=50, required= True, label="Author")
    price = forms.DecimalField(required=True, label="Price", initial=0)
    edition = forms.IntegerField(required=True, initial=10, widget=forms.NumberInput())

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','age','address']
    name = forms.CharField(max_length=50, required=True, label="name")
    age = forms.DecimalField(required=True, label="age", initial=18)
    address = forms.ModelChoiceField(label = "address", queryset=Address.objects.all())


class StudentForm2(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']
    name = forms.CharField(max_length=50, required=True, label="name")
    age = forms.DecimalField(required=True, label="age", initial=18)
    addresses = forms.ModelMultipleChoiceField(label='addresses', queryset=Address2.objects.all(), widget=forms.CheckboxSelectMultiple())

from .models import ImageEntry

class ImageEntryForm(forms.ModelForm):
    class Meta:
        model = ImageEntry
        fields = ['title', 'image', 'description']