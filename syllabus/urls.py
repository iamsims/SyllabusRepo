from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='syllabus-home'),#go to select part , for now only this to be handled
    path('about/',views.about,name='syllabus-about'),#add about section to give information about the repository
    path('login/',auth_views.LoginView.as_view(template_name='syllabus/login.html'),name='syllabus-login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='syllabus/logout.html'),name='syllabus-logout'),
    path('add/',views.add,name='add-syllabus'),#path when form is to be added
    path('<int:pk>/',views.topics,name='topics'),#this is to view full syllabus, make table
    path('addsub/',views.addsub,name='add-subject'),
    path('addspec/',views.addspec,name='add-specs'),
    # path('uploadpdf/',views.addsub,name='upload-pdf'),
    path('edit/<int:pk>/',views.add,name='update'),
    path('delete/<int:pk>/',views.delete,name='delete')
]