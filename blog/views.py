from dataclasses import fields
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView

from .models import Post



# моть, это полезная фигня,прочитай по книге на сервере и на стр 87 вроде
# описан план действий. развей этот файл до корректной работы со стороннего по и 
# наладь работу с базой данных. Есть sqlalchemy, вот он очень поможет в этом деле
# зп отдам вовремя, в прошедшем месяце у тебя эффективность упала, поэтому оплата всего 300$ 

class PostCreate(CreateView):
    model = Post
    fields = ("name", "description")
    template_name = "create.html"
    success_url = "/"
    
class PostList(ListView):
    model = Post
    template_name = "list.html"
    
class PostDetail(DetailView):
    model = Post
    template_name = "detail.html"
    
class PostUpdate(UpdateView):
    model = Post
    fields = ("name", "description")
    template_name = "update.html"
    success_url = "/"
    
class PostDelete(DeleteView):
    model = Post
    success_url = "/"
