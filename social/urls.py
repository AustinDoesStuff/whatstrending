from django.conf.urls import url
from . import views

#app_name = 'social'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^json/', views.JsonView.as_view()),
]