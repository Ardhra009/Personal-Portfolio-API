"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from api.views import aboutView,EducationView,projectView,SkillsView,ExperienceView,CertificationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',aboutView.as_view()),
    path('education/',EducationView.as_view()),
    path('project/',projectView.as_view()),
    path('skill/',SkillsView.as_view()),
    path('experience/',ExperienceView.as_view()),
    path('certficate/',CertificationView.as_view())
]
