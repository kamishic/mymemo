from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.MemoCreateView.as_view(),name="memo_create"),
    path('list',views.MemoListView.as_view()),
]