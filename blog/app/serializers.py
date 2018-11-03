from rest_framework import serializers

from app.models import Culumn


class CulumnSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(required=True,error_messages={'required': 'title辟邪'})
    class Meta:
        # 指定序列化模型
        model = Culumn
        # 序列化字段
        fields = ['id']
