from django.urls import path, include
from .views import NewsList, NewsDetail,NewsSearch,NewsCreate,PostUpdate,PostDelete,ArticleCreate, upgrade_me


urlpatterns = [
    path('', NewsList.as_view(), name = 'news_list'),
    path('<int:pk>/',NewsDetail.as_view(), name = 'news_detail'),
    path('news/search/', NewsSearch.as_view(), name = 'news_search'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', PostUpdate.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='article_delete'),
    path('accounts/', include('allauth.urls')),
    path('upgrade/', upgrade_me, name = 'upgrade'),

]