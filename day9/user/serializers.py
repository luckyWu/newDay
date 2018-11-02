from rest_framework import serializers
from user.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(required=True,error_messages={'required': 'title辟邪'})

    class Meta:
        # 指定序列化模型
        model = Article
        # 序列化字段
        fields = ['title', 'desc','id']
