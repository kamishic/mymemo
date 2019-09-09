from django.urls import path,include
from . import views

app_name="memo"
urlpatterns = [
    path('',views.MemoIndexView.as_view(),name="memo_index"),
    path('add',views.MemoCreateView.as_view(),name="memo_create"),    
    path('list',views.MemoListView.as_view()),
]