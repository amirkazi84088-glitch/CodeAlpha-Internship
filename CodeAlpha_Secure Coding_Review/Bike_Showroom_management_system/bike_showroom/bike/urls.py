

# bike/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Public
    path('', views.home, name='home'),
    path('about/',    views.about,    name='about'),
    path('services/', views.services, name='services'),
    path('contact/',  views.contact,  name='contact'),
    path('book/',     views.book,     name='book'),
    # Auth

    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),


    path('profile/', views.profile, name='profile'),

    # Bike CRUD
    path('admin/bikes/',               views.bike_list,   name='bike_list'),
    path('admin/bikes/add/',           views.bike_create, name='bike_create'),
    path('admin/bikes/<int:pk>/edit/', views.bike_update, name='bike_update'),
    path('admin/bikes/<int:pk>/del/',  views.bike_delete, name='bike_delete'),
]
