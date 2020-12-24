from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home import views
urlpatterns = [
  path("", views.index,name='home'),  
   
  path("about", views.about,name='about'),  
  path("bestseller", views.bestseller,name='bestseller'),
  path("contacts", views.contacts,name='contacts'),
  path("tracker", views.tracker,name='tracker'),
  path("books<int:myid>", views.bookView,name='BookView'),
   path("checkout", views.checkout,name='checkout'),  
  path("me", views.me,name='me'), 
  path("signup", views.handleSignup,name='handleSignup'),
  path("login", views.handleLogin,name='handleLogin'),
  path("logout", views.handleLogout,name='handleLogout'),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
