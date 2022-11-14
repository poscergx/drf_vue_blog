from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAdminUser
# from rest_framework import generics
# from rest_framework import mixins
# from rest_framework import status
#
# from django.http import JsonResponse
# from django.http import Http404
#
# from article.serializers import ArticleDetailSerializer
# from article.serializers import ArticleListSerializer
from article.models import Article
from article.permissions import IsAdminUserOrReadOnly
#
#
# # Create your views here.
#
# # 基于方法的视图
# # def article_list(request):
# #     articles = Article.objects.all()
# #     serializer = ArticleListSerializer(articles, many=True)
# #     return JsonResponse(serializer.data, safe=False)
#
# # @api_view(['GET', 'POST'])
# # def article_list(request):
# #     if request.method == 'GET':
# #         articles = Article.objects.all()
# #         serializer = ArticleListSerializer(articles, many=True)
# #         return JsonResponse(serializer.data, safe=False)
# #
# #     elif request.method == 'POST':
# #         serializer = ArticleListSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # 基于类的视图案例
# # @permission_classes((IsAdminUser,))
# @permission_classes((IsAdminUserOrReadOnly,))
# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleListSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)
#
#
# # class ArticleDetail(APIView):
# #     """文章详情视图"""
# #
# #     def get_object(self, pk):
# #         """获取单个文章对象"""
# #         try:
# #             # pk 即主键，默认状态下就是 id
# #             return Article.objects.get(pk=pk)
# #         except:
# #             raise Http404
# #
# #     def get(self, request, pk):
# #         article = self.get_object(pk)
# #         serializer = ArticleDetailSerializer(article)
# #         # 返回 Json 数据
# #         return Response(serializer.data)
# #
# #     def put(self, request, pk):
# #         article = self.get_object(pk)
# #         serializer = ArticleDetailSerializer(article, data=request.data)
# #         # 验证提交的数据是否合法
# #         # 不合法则返回400
# #         if serializer.is_valid():
# #             # 序列化器将持有的数据反序列化后，
# #             # 保存到数据库中
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #
# #     def delete(self, request, pk):
# #         article = self.get_object(pk)
# #         article.delete()
# #         # 删除成功后返回204
# #         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# # 通用视图简化请求一
# # class ArticleDetail(mixins.RetrieveModelMixin,
# #                     mixins.UpdateModelMixin,
# #                     mixins.DestroyModelMixin,
# #                     generics.GenericAPIView):
# #     """文章详情视图"""
# #     queryset = Article.objects.all()
# #     serializer_class = ArticleDetailSerializer
# #
# #     def get(self, request, *args, **kwargs):
# #         return self.retrieve(request, *args, **kwargs)
# #
# #     def put(self, request, *args, **kwargs):
# #         return self.update(request, *args, **kwargs)
# #
# #     def delete(self, request, *args, **kwargs):
# #         return self.destroy(request, *args, **kwargs)
#
# # 通用视图简化二
# @permission_classes((IsAdminUserOrReadOnly,))
# class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleDetailSerializer

from rest_framework import viewsets
from article.serializers import ArticleSerializer


# @permission_classes((IsAdminUserOrReadOnly,))
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
