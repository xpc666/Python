from django.shortcuts import render, reverse
from django.views import View
from django.views.generic.edit import CreateView
from books import models
from books.forms import NewPublisher, BookForm, CatalogForm

# Create your views here.

def index(request):
    # check if user has logged in. If not, direct to the login page.
    return render(request,'books/index.html')
    # return reverse(request, 'books/index.html')

class PublisherView(View):
    def get(self, request):
        publst = models.Publisher.objects.all()
        context = {'publisher':publst}
        return render(request,'books/publisherpage.html', context)

    def post(self, request):
        toDeleteList = request.POST.getlist ('publisherToDelete')
        for pb_id in toDeleteList:
            models.Publisher.objects.filter(id=pb_id).delete()

        return self.get(request)

class BookView(View):
    def get(self, request):
        bklst = models.Book.objects.all()
        context = {'book':bklst}
        return render(request, 'books/bookpage.html', context)

    def post(self, request):
        toDeleteList = request.POST.getlist ('booksToDelete')
        for bk_id in toDeleteList:
            models.Book.objects.filter(bookid=bk_id).delete()

        return self.get(request)

class CatalogView(View):
    def get(self, request):
        catalst = models.Catalog.objects.all()
        context = {'catalog':catalst}
        return render(request, 'books/catalogpage.html', context)

    def post(self, request):
        toDeleteList = request.POST.getlist ('catalogsToDelete')
        for ct_id in toDeleteList:
            models.Catalog.objects.filter(catalog_id=ct_id).delete()

        return self.get(request)

class CatalogCreateView(CreateView):
    template_name = 'books/addCatalog.html'
    form_class = CatalogForm

def addpublisher(request):
    form = NewPublisher()

    if request.method == 'POST':
        form = NewPublisher(request.POST)

        if form.is_valid():
            form.save(commit=True)
            publst = models.Publisher.objects.all()
            return render(request, 'books/publisherpage.html', {'publisher': publst})

    return render(request, 'books/addpublisher.html', {'form':form, 'joytest': 'Hello Joy!'})

def addBook(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            bklst = models.Book.objects.all()
            return render(request, 'books/bookpage.html', {'book':bklst})

    return render(request, 'books/addBook.html', {'form':form})

def deleteBooks(request):
    CHOICE = ['apple', 'banana', 'orange', 'pear']
    if request.method == 'POST':
        toDeleteList = request.POST.getlist ('booksToDelete')
        for bk_id in toDeleteList:
            models.Book.objects.filter(bookid=bk_id).delete()

        fruitRemoveList = request.POST.getlist ('fruitToRemove')
        for frt in fruitRemoveList:
            CHOICE.remove(frt)

    bklst = models.Book.objects.all()
    # context = {'book':bklst}
    context = {'book':bklst, 'fruit':CHOICE}
    return render(request, 'books/bookpage.html', context)
