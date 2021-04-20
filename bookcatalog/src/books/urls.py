from django.urls import path
from books import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='home'),
    path('publisherpage', views.PublisherView.as_view(), name='publisherpage'),
    path('bookpage', views.BookView.as_view(), name='bookpage'),
    path('catalogpage', views.CatalogView.as_view(), name='catalogpage'),
    path('newpublisher', views.addpublisher, name='newpublisher'),
    path('newbook', views.addBook, name='newbook'),
    path('newcatalog', views.CatalogCreateView.as_view(), name='newcatalog'),
]
