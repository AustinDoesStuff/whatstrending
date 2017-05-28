from django.conf.urls import url
from . import views

#app_name = 'social'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^json/twitter/', views.TwitterJsonView.as_view()),
    url(r'^json/reddit/', views.RedditJsonView.as_view()),
]