from django.urls import include, path

from . import views

urlpatterns = [
  path('', views.ReviewListView.as_view(), name='review-list-view')
]
