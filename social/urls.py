from django.conf.urls import url
from . import views

#app_name = 'social'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^json/', views.JsonView.as_view()),
]