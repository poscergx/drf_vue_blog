from rest_framework import serializers
from article.models import Article, Category

from user_info.serializers import UserDescSerializer


class CategorySerializer(serializers.ModelSerializer):
    """分类的序列化器"""
    url = serializers.HyperlinkedIdentityField(view_name='category-detail')

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created']


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    """博文序列化器"""
    author = UserDescSerializer(read_only=True)
    # category 的嵌套序列化字段
    category = CateGorySerializer(read_only=True)
    # category 的 id 字段，用于创建/更新 category 外键
    category_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)

    # category_id 字段的验证器
    def validate_category_id(self, value):
        if not Category.objects.filter(id=value).exists() and value is not None:
            raise serializers.ValidationError("Category with id {} not exists.".format(value))
        return value

    class Meta:
        model = Article
        fields = '__all__'


class ArticleCategoryDetailSerializer(serializers.ModelSerializer):
    """给分类详情的嵌套序列化器"""
    url = serializers.HyperlinkedIdentityField(view_name='article-detail')

    class Meta:
        model = Article
        fields = [
            'url',
            'title',
        ]


class CategoryDetailSerializer(serializers.ModelSerializer):
    """分类详情"""
    articles = ArticleCategoryDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'created',
            'articles',
        ]

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
