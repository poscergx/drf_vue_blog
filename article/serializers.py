from rest_framework import serializers
from article.models import Article

from user_info.serializers import UserDescSerializer


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = UserDescSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'

# class ArticleListSerializer(serializers.ModelSerializer):
#     # 新增字段，添加超链接
#     url = serializers.HyperlinkedIdentityField(view_name="article:detail")
#     # read_only 参数设置为只读
#     author = UserDescSerializer(read_only=True)
#
#     class Meta:
#         model = Article
#         fields = [
#             'url',
#             # 有了url之后，就不需要id了
#             # 'id',
#             'title',
#             'created',
#             'author'
#         ]
#
#         # 嵌套序列化器已经设置了只读，所以这个就不要了
#         # read_only_fields = ['author']


# class ArticleDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
