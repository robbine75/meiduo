"""meiduo_mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),   # 站点管理
    url(r'^', include('verifications.urls')),    # 短信模块路由
    url(r'^', include('users.urls')),    # 用户模块路由
    url(r'^oauth/',include('oauth.urls')), # qq登陆模块
    url(r'^',include('areas.urls')),     # 省市区路由
    url(r'^ckeditor/', include('ckeditor_uploader.urls')), # 富文本编辑器
    url(r'^', include('goods.urls')),   # 商品
    url(r'^', include('carts.urls')),   # 购物车
    url(r'^', include('orders.urls')),  # 订单
    url(r'^', include('payment.urls')), # 支付宝支付
]
