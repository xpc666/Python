from django.urls import path
from books import views

app_name = 'books'

urlpatterns = [

    path('publisherpage', views.PublisherView.as_view(), name='publisherpage'),
    # path('bookpage', views.BookView.as_view(), name='bookpage'),
    path('bookpage', views.BookListView.as_view(), name='bookpage'),
    path('genrepage', views.GenreView.as_view(), name='genrepage'),
    path('newpublisher', views.addpublisher, name='newpublisher'),
    path('newbook', views.addBook, name='newbook'),
    path('newgenre', views.GenreCreateView.as_view(), name='newgenre'),
    path('<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    # path('<int:pk>/', views.get_book_detail, {'book_detail.html': 'books/'}, name='book-detail'),
]
