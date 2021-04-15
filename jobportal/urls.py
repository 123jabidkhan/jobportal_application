"""jobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from job import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('admin_login/',views.admin_login, name='admin_login'),
    path('recruiter_login/',views.recruiter_login, name='recruiter_login'),
    path('user_login/',views.user_login, name='user_login'),
    path('contact/',views.contact, name='contact'),

    path('student_signup/',views.student_signup, name='student_signup'),
    path('recruiter_signup/',views.recruiter_signup, name='recruiter_signup'),
    path('student_profile/',views.student_profile, name='student_profile'),
    path('recruiter_profile/',views.recruiter_profile, name='recruiter_profile'),
    path('admin_profile/',views.admin_profile, name='admin_profile'),
    path('view_users/',views.view_users, name='view_users'),   
    path('recruiter_pending/',views.recruiter_pending, name='recruiter_pending'),
    path('recruiter_accept/',views.recruiter_accept, name='recruiter_accept'),
    path('recruiter_reject/',views.recruiter_reject, name='recruiter_reject'),
    path('recruiter_all/',views.recruiter_all, name='recruiter_all'),
    path('change_status/<int:id>',views.change_status, name='change_status'),
    path('addjob/',views.addjob, name='addjob'),
    path('joblist/',views.joblist, name='joblist'),



    path('user_delete/<int:id>',views.user_delete, name='user_delete'),
    path('recruiter_delete/<int:id>',views.recruiter_delete, name='recruiter_delete'),
    path('all_logout/',views.all_logout, name='all_logout'),
    





]
