from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.links, name = "books.html5.links"),
    path('html5/text/Formatting/', views.formatting, name= 'books.html5.formating'),
    path('html5/Listing/', views.listing, name= 'books.html5.Listing'),
    path('html5/tables/',views.tables, name= 'books.html5.tables'),
]