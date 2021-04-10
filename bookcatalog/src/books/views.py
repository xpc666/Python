from django.shortcuts import render
from django.views import View
from books import models
from books.forms import NewPublisher

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

def deleteBooks(request):
    if request.method == 'POST':
        toDeleteList = request.POST.getlist ('booksToDelete')
        for bk_id in toDeleteList:
            Book.objects.filter(bookid=bk_id).delete()

    bklst = models.Book.objects.all()
    context = {'book':bklst}
    return render(request, 'bookpage.html', context)
