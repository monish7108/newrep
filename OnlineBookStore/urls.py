from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'top-authors-and-their-works/', views.top_authors_and_works, name="top-authors-and-their-works"),

    url(r'^authors/rest/$', views.authors_list_rest, name="authorList"),
    # url(r'^books/rest/$', views.books_list_rest, name="bookList"),
    # url(r'^books-of-author/rest/(?P<author_id>\d+)$', views.authors_work_rest, name="authorsWorks"),
    # url(r'^top-ten-books/rest/$', views.top_ten_books_rest, name="topTenBooks"),
    # url(r'^author-of-the-year/rest/(?P<year>\d+)', views.author_of_the_year_rest, name="authorOfTheYear"),
    #
    # url(r'^authors/$', views.authors_list, name="authorList"),
    # url(r'^books/$', views.books_list, name="bookList"),
    # url(r'^books-of-author/(?P<author_id>\d+)$', views.authors_work, name="authorsWorks"),
    # url(r'^top-ten-books/$', views.top_ten_books_rest, name="topTenBooks"),
    # url(r'^author-of-the-year/(?P<year>\d+)', views.author_of_the_year_rest, name="authorOfTheYear"),
]