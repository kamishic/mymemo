#from django.shortcuts import render
from django.views.generic import ListView,TemplateView,CreateView
from .models import BookMemo,Book
from django.urls import reverse_lazy
# Create your views here.
class MemoIndexView(TemplateView):
    template_name="memo/index.html"

class MemoCreateView(CreateView):
    model=BookMemo
    fields="__all__"
    template_name = 'memo/MemoCreate.html'
    success_url = reverse_lazy('memo_create')


class MemoListView(ListView):
    model = BookMemo