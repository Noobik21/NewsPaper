import django_filters
from .models import Post
from django.forms import DateInput

class PostFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Название'
    )

    author = django_filters.CharFilter(
        field_name='author__user__username',
        lookup_expr='icontains',
        label='Автор'
    )

    date = django_filters.DateFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='После даты',
        widget=DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Post
        fields = ['title', 'author', 'date']