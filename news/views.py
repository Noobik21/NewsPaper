from django.views.generic import ListView, CreateView
from .models import Post
from django.views.generic import DetailView
from django_filters.views import FilterView
from .filters import PostFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from.forms import PostForm
from django.views.generic.edit import DeleteView

@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name = 'authors')
    user.groups.add(authors_group)
    return redirect('/')

class NewsList(ListView):
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    ordering = ['-created']
    paginate_by = 10

class NewsDetail(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = 'post'


class NewsSearch(FilterView):
    model = Post
    template_name = 'news_search.html'
    filterset_class = PostFilter
    paginate_by = 10
#Createnews
class NewsCreate(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    permission_required = ('news.add_post',)


    def form_valid(self, form):
        post = form.save(commit = False)
        post.postType = 'NW'
        return super().form_valid(form)
#CreatePost
class ArticleCreate(PermissionRequiredMixin,CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    permission_required = ('news.add_post',)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.postType = 'AR'
        return super().form_valid(form)
#Edit
class PostUpdate(PermissionRequiredMixin,LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    permission_required = ('news.change_post',)
#Delete
class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = '/news/'


