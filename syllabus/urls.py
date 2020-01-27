from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='syllabus-home'),#go to select part , for now only this to be handled
    path('about/',views.about,name='syllabus-about'),#add about section to give information about the repository
    path('login/',auth_views.LoginView.as_view(template_name='syllabus/login.html'),name='syllabus-login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='syllabus/logout.html'),name='syllabus-logout'),
    path('<int:pk>/',views.SyllabusView.as_view(),name='syllabus-subjects')
]