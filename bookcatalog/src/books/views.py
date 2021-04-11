from django.shortcuts import render
from django.views import View
from books import models
from books.forms import NewPublisher, BookForm

# Create your views here.

def index(request):
    return render(request,'index.html')

class PublisherView(View):
    def get(self, request):
        publst = models.Publisher.objects.all()
        context = {'publisher':publst}
        return render(request,'publisherpage.html', context)

class BookView(View):
    def get(self, request):
        bklst = models.Book.objects.all()
        context = {'book':bklst}
        return render(request, 'bookpage.html', context)

def addpublisher(request):
    form = NewPublisher()

    if request.method == 'POST':
        form = NewPublisher(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'index.html')

    return render(request, 'addpublisher.html', {'form':form, 'joytest': 'Hello Joy!'})

def addBook(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'index.html')

    return render(request, 'addBook.html', {'form':form})

def deleteBooks(request):
    print("i am reached 1")
    CHOICE = ['apple', 'banana', 'orange', 'pear']
    if request.method == 'POST':
        print("i am reached 2")
        toDeleteList = request.POST.getlist ('booksToDelete')
        print(toDeleteList)
        for bk_id in toDeleteList:
            print("i am reached 3")
            models.Book.objects.filter(bookid=bk_id).delete()

        fruitRemoveList = request.POST.getlist ('fruitToRemove')
        for frt in fruitRemoveList:
            CHOICE.remove(frt)

    bklst = models.Book.objects.all()
    # context = {'book':bklst}
    context = {'book':bklst, 'fruit':CHOICE}
    return render(request, 'bookpage.html', context)
