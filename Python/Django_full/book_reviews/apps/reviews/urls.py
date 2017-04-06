from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books$', views.books, name='books'),
    url(r'^books/add$', views.add, name='add'),

    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^add_book$', views.add_book, name='add_book'),
    url(r'^book_display/(?P<book_id>\d+)$', views.book_display, name='book_display'),
    url(r'^user/(?P<user_id>\d+)$', views.user_display, name='user_display'),
]
