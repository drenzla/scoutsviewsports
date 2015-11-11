"""scoutsviewsports URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from website import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^coach_signup/$', views.coach_signup, name='as_coach'),
	url(r'^fan_signup/$', views.fan_signup, name='as_fan'),
    url(r'^coach2a/$', views.coach2a, name='coach2a'),
    url(r'^coach2b/$', views.coach2b, name='coach2b'),
    url(r'^coach_pg1/$', views.coach_pg1, name='coach_pg1'),
    url(r'^coach_home/$', views.coach_pg2, name='coach_pg2'),
    url(r'^coach_pg3/$', views.coach_pg3, name='coach_pg3'),
    url(r'^coach_pg4/$', views.coach_pg4, name='coach_pg4'),
    url(r'^coach_pg5/$', views.coach_pg5, name='coach_pg5'),
    url(r'^coach_pg6/$', views.coach_pg6, name='coach_pg6'),
    url(r'^coach_pg7/$', views.coach_pg7, name='coach_pg7'),
    url(r'^coach_pg8/$', views.coach_pg8, name='coach_pg8'),
    url(r'^coach_pg9/$', views.coach_pg9, name='coach_pg9'),
    url(r'^coach_pg10/$', views.coach_pg10, name='coach_pg10'),
    url(r'^coach_pg12/$', views.coach_pg12, name='coach_pg12'),
    url(r'^inner1/$', views.inner, name='inner'),
    url(r'^athlete_home/$', views.inner2, name='inner2'),
    url(r'^message/$', views.message, name='message'),
    url(r'^search/$', views.search, name='search'),
]
