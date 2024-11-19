from django.shortcuts import render, redirect
from .models import Book, Student, address
from django.db.models import Q, Sum, Avg, Max, Min, Count
from .forms import BookForm

def index(request):
 return render(request, "bookmodule/index.html")

def list_books(request):
 return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
 return render(request, 'bookmodule/one_book.html')

def aboutus(request):
 return render(request, 'bookmodule/aboutus.html')

def links(request):
 return render(request, 'bookmodule/links.html')

def formatting(request):
 return render(request, 'bookmodule/Formatting.html')

def listing(request):
 return render(request, 'bookmodule/Listing.html')

def tables(request):
 return render(request, 'bookmodule/tables.html')

def search(request):
 if request.method == "POST":
    string = request.POST.get('keyword').lower()
    isTitle = request.POST.get('option1')
    isAuthor = request.POST.get('option2')
    # now filter
    books = __getBooksList()
    newBooks = []
    for item in books:
        contained = False
        if isTitle and string in item['title'].lower(): contained = True
        if not contained and isAuthor and string in item['author'].lower():contained = True
        if contained: newBooks.append(item)
    return render(request, 'bookmodule/bookList.html', {'books':newBooks})
 return render(request, 'bookmodule/search.html')

def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and')
    return render(request,'bookmodule/bookList.html', {"books":mybooks})

def lookup_query(request):
    mybooks=Book.objects.filter(author__isnull=False).filter(title__icontains='and').exclude(price__lte=100.00) [:10]
    if len(mybooks) >=1:
        return render(request,'bookmodule./bookList.html',{'books':mybooks})
    else:
        return render(request,"bookmodule/index.html")

def __getBooksList():
 book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
 book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
 book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
 return [book1, book2, book3]

def task1(request):
 mybook = Book.objects.filter(price__lte=50)
 return render(request,'bookmodule/booklist.html',{'title':'books with price less than 50','books':mybook})

def task2(request):
  mybook = Book.objects.filter(Q(edition__gt=2) & (Q(title__contains='qu') | Q(author__contains='qu')))
  return render(request,'bookmodule/booklist.html',{'title':'books with edtion higher than 2 and contain "qu" in title or author','books':mybook})

def task3(request):
  mybook = Book.objects.filter(~Q(edition__gt=2) & (~Q(title__contains='qu') | ~Q(author__contains='qu')))
  return render(request,'bookmodule/booklist.html',{'title':'books with no edtion higher than 2 and dont contain "qu" in title or author','books':mybook})

def task4(request):
  mybook = Book.objects.order_by('title')
  return render(request,'bookmodule/booklist.html',{'title':'books with edtion higher than 2 and contain "qu" in title or author','books':mybook})

def task5(request):
  NoB = Book.objects.count()
  query = Book.objects.aggregate(total_price=Sum('price',default=0), average_price=Avg('price',default=0), 
                                 maximum_price=Max('price',default=0),minimumm_price=Min('price',default=0))
  return render(request,'bookmodule/aggergatequery.html',{'title':'the number of books, total price of all books, average price, maximum price, and minimum price','NoB':NoB,'query':query})

def task7(request):
  cities = (address.objects.annotate(student_count=Count('student')).values('address', 'student_count'))  
  return render(request, 'bookmodule/listStudent.html', {'cities':cities})

def singleBook(request, Id):
 mybook = Book.objects.get(id = Id)
 return render(request, 'bookmodule/show.html',{'book':mybook})

def listbooks(request):
  mybook = Book.objects.all()
  return render(request,'bookmodule/listBooks.html', {'books':mybook})

def addbook(request):
  if request.method == 'POST':
    title = request.POST.get('title')
    author = request.POST.get('author')
    price = request.POST.get('price')
    edition = request.POST.get('edition')
    newobj = Book(title=title, author=author, price=price, edition=edition)
    newobj.save()
    return redirect('books.l9p1t1')
  return render(request, 'bookmodule/addBook.html')

def editbook(request, Id):
  mybook = Book.objects.get(id=Id)
  if request.method == 'POST':
    title = request.POST.get('title')
    author = request.POST.get('author')
    price = request.POST.get('price')
    edition = request.POST.get('edition')
    mybook.title = title
    mybook.author = author
    mybook.price = float(price)
    mybook.edition = int(edition)
    mybook.save()
    return redirect('books.l9p1t1')
  return render(request, 'bookmodule/editbook.html', {'book':mybook})

def deleteBook(request, Id):
  mybook=Book.objects.get(id = Id)
  mybook.delete()
  return redirect('books.l9p1t1')

def listbooks_django(request):
  mybook = Book.objects.all()
  return render(request,'bookmodule/listBooks_django.html', {'books':mybook})

def addbook_django(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books.l9p2t1')
    else:
        form = BookForm()
    return render(request, 'bookmodule/addBook_django.html', {'form': form})

def editbook_django(request, Id):
    mybook = Book.objects.get(id=Id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=mybook)
        if form.is_valid():
            form.save()
            return redirect('books.l9p2t1')
    else:
        form = BookForm(instance=mybook)
    return render(request, 'bookmodule/editbook_django.html', {'form': form})

def deleteBook_django(request, Id):
  mybook = Book.objects.get(id=Id)
  mybook.delete()
  return redirect('books.l9p2t1')