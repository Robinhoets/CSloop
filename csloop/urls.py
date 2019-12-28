# csloop/urls.py

from django.urls import path

from .views import CsloopListView

urlpatterns = [
	path('', CsloopListView.as_view(), name='home'),
]

