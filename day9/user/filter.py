import django_filters
from user.models import Article
from rest_framework import filters


class ArticleFilter(filters.FilterSet):
    t = django_filters.CharFilter('title',lookup_expr='icontains')#不区分大小写；
    desc = django_filters.CharFilter('desc',lookup_expr='contains')#'gt'
    min= django_filters.DateFilter('create_time', lookup_expr='gt')  # 'gt'
    class Meta:
        model = Article
        fields = []
