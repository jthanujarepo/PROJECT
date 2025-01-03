from django.urls import path
from .views import *
urlpatterns = [
    path('signup/',view=SignupView),
    path('home/',view=home),
    path('login/',view=loginview),
    path('book/<str:bookid>',get_book),
    path('contact/',view=contactview,name='contact'),
    path('mail/',view=mail),

    path('product/' ,view=product),
    path("bookview/",BookView.as_view(),name='list'),
    path("bookview2/",BookView2.as_view(),),
    path("update/<int:pk>",booksupdate.as_view() ,name='update'),
    path('bookdelete/<int:pk>',booksdelete.as_view(),name='delete'),
    path('fictionapi/',FictionAPI.as_view()),
    path('fictionapi/<int:pk>/',FictionAPI.as_view()),
    path('collections',view=collections,name="collections"),
    path('collections/<str:title>',view=collectionsview,name="collections"),
    path('imageupdate/',imageupdate),
]
