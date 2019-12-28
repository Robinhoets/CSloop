from django.shortcuts import render
from django.views.generic import ListView

from .models import Post


class CsloopListView(ListView):
	model = Post
	template_name = 'home.html'
