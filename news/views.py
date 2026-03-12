from django.views.generic import ListView
from .models import Post
from django.views.generic import DetailView
from django_filters.views import FilterView
from .filters import PostFilter

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
class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit = False)
        post.postType = 'NW'
        return super().form_valid(form)
#CreatePost
class ArticleCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.postType = 'AR'
        return super().form_valid(form)
#Edit
class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
#Delete
class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = '/news/'