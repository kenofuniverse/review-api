from django.urls import include, path

from . import views

urlpatterns = [
  path('', views.CompanyListView.as_view(), name='company-list-view')
]
