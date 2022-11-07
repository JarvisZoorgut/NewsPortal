from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter
from django.forms import DateTimeInput
from .models import Post, Category


class PostFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name = 'postcategory__categoryThrough',
        queryset = Category.objects.all(),
        label = 'Категория',
        empty_label = 'Все категории'
    )

    added_after = DateTimeFilter(
        field_name='postTime',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }