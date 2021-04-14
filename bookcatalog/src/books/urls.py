from django.contrib import admin
from django.urls import path, include
from books import views

urlpatterns = [
    path('publisherpage', views.PublisherView.as_view(), name='publisherpage'),
    path('bookpage', views.BookView.as_view(), name='bookpage'),
    # path('bookpage.html', views.deleteBooks, name='list_delete'),
    path('newpublisher', views.addpublisher, name='newpublisher'),
    path('newbook', views.addBook, name='newbook'),
]
