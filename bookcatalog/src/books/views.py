from django.shortcuts import render, reverse
from django.views import View
from django.views.generic.edit import CreateView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from books import models
from books.forms import NewPublisher, BookForm, GenreForm

# Create your views here.

@login_required
def index(request):
    # check if user has logged in. If not, direct to the login page.
    return render(request,'index.html')
    # return reverse(request, 'books/index.html')

class PublisherView(LoginRequiredMixin, View):
    def get(self, request):
        publst = models.Publisher.objects.all()
        context = {'publisher':publst}
        return render(request,'books/publisherpage.html', context)

    def post(self, request):
        toDeleteList = request.POST.getlist ('publisherToDelete')
        for pb_id in toDeleteList:
            models.Publisher.objects.filter(id=pb_id).delete()

        return self.get(request)

class BookView(LoginRequiredMixin, View):
    def get(self, request):
        bklst = models.Book.objects.all()
        context = {'book_list':bklst}
        return render(request, 'books/bookpage.html', context)

    def post(self, request):
        toDeleteList = request.POST.getlist ('booksToDelete')
        for bk_id in toDeleteList:
            models.Book.objects.filter(id=bk_id).delete()

        return self.get(request)

class BookListView(generic.ListView):
    model = models.Book

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the context
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     # Create any data and add it to the context
    #     context['some_data'] = 'This is just some data'
    #     return context

from django.shortcuts import get_object_or_404

def get_book_detail(request, id):
    book = get_object_or_404(models.Book, pk=id)
    return render(request, 'books/book_detail.html', context={'book': book})

class GenreView(LoginRequiredMixin, View):
    def get(self, request):
        catlst = models.Genre.objects.all()
        context = {'genre':catlst}
        return render(request, 'books/genrepage.html', context)

    def post(self, request):
        toDeleteList = request.POST.getlist ('genreToDelete')
        for cat in toDeleteList:
            models.Genre.objects.filter(name=cat).delete()

        return self.get(request)

class GenreCreateView(LoginRequiredMixin, CreateView):
    template_name = 'books/addGenre.html'
    form_class = GenreForm

class BookDetailView(generic.DetailView):
    model = models.Book

    # def book_detail_view(request, primary_key):
    #     try:
    #         book = Book.objects.get(pk=primary_key)
    #     except Book.DoesNotExist:
    #         raise Http404('Book does not exist')
    # return render(request, 'catalog/book_detail.html', context={'book': book})

@login_required
def addpublisher(request):
    form = NewPublisher()

    if request.method == 'POST':
        form = NewPublisher(request.POST)

        if form.is_valid():
            form.save(commit=True)
            publst = models.Publisher.objects.all()
            return render(request, 'books/publisherpage.html', {'publisher': publst})

    return render(request, 'books/addpublisher.html', {'form':form, 'joytest': 'Hello Joy!'})

@login_required
def addBook(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            bklst = models.Book.objects.all()
            return render(request, 'books/bookpage.html', {'book':bklst})

    return render(request, 'books/addBook.html', {'form':form})

@login_required
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
