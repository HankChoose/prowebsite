from django.urls import path
from . import views

app_name='encyclopedia'
#<a href="{% url 'encyclopedia:index' %}">View Index</a>

urlpatterns = [
    #path("", views.hankview, name="hankview"),
    #path("", views.index, name="index"),
    path('random/', views.random_page, name='random_page'),
    path("searchfrom", views.searchfrom, name="searchfrom"),
    path("search", views.search, name="search"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("wiki/<str:title>/edit/", views.entryedit, name="entryedit"),
    path("entryadd", views.entryadd, name="entryadd"),
]

