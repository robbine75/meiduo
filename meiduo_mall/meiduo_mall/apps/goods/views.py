from django.shortcuts import render

# Create your views here.
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.response import Response

from .models import SKU, GoodsCategory
from .serializers import SKUSerializer


# class CategoryView(GenericAPIView):
#     """
#     商品列表页面包屑导航
#     """
#     queryset = GoodsCategory.objects.all()
#
#     def get(self, request, pk=None):
#         ret = dict(
#             cat1='',
#             cat2='',
#             cat3=''
#         )
#         category = self.get_object()
#         if category.parent is None:
#             # 当前类别为一级类别
#             ret['cat1'] = ChannelSerializer(category.goodschannel_set.all()[0]).data
#         elif category.goodscategory_set.count() == 0:
#             # 当前类别为三级
#             ret['cat3'] = CategorySerializer(category).data
#             cat2 = category.parent
#             ret['cat2'] = CategorySerializer(cat2).data
#             ret['cat1'] = ChannelSerializer(cat2.parent.goodschannel_set.all()[0]).data
#         else:
#             # 当前类别为二级
#             ret['cat2'] = CategorySerializer(category).data
#             ret['cat1'] = ChannelSerializer(category.parent.goodschannel_set.all()[0]).data
#
#         return Response(ret)


class SKUListView(ListAPIView):
    """商品列表界面"""

    # 指定序列化器
    serializer_class = SKUSerializer

    # 指定过滤后端为排序?
    filter_backends = [OrderingFilter]

    # 指定排序字段
    ordering_fields = ['create_time', 'price', 'sales']

    # 指定查询集
    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return SKU.objects.filter(is_launched=True, category_id=category_id)