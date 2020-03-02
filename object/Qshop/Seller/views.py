from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect,HttpResponse
import hashlib
from django.core.paginator import Paginator
import random

# Create your views here.

# 退出
def logout(request):
    response = HttpResponseRedirect('/Seller/login/')
    response.delete_cookie('email')
    del request.session['email']
    return response

# 密码加密
def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result

# 登录装饰器
def loginValid(func):
    def inner(request,*args,**kwargs):
        cookie_email = request.COOKIES.get('email')
        session_email = request.session.get('email')
        if cookie_email and session_email and cookie_email == session_email:
            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/Seller/login/')
    return inner

# 注册
def register(request):
    # 接受参数
    if request.method == 'POST':
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        email = request.POST.get('email')
        # 校验数据
        if email and password and password == repassword:
            LoginUser.objects.create(email=email,password=setPassword(password),user_type=0)
            return HttpResponseRedirect('/Seller/login/')
        else:
            megass = '输入错误'
    return render(request,'seller/register.html',locals())

# 登录功能
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            user = LoginUser.objects.filter(email=email,user_type=0,password=setPassword(password)).first()
            if user:
                response = HttpResponseRedirect('/Seller/index/')
                response.set_cookie('email',user.email)
                response.set_cookie('userid',user.id)
                request.session['email'] = user.email
                return response
            else:
                message = '账号密码不正确'
        else:
            message = '参数为空'
    return render(request,'seller/login.html',locals())

# 首页
@loginValid
def index(request):
    return render(request,'seller/index.html')

# 商品列表页
@loginValid
def goods(request,status,page=1):

    # goods = Goods.objects.all()
    # goods = Goods.objects.filter(goods_status=status).order_by('id')
    goods = Goods.objects.filter(goods_status=status,goods_store=request.COOKIES.get('userid')).order_by('id')
    goods_obj = Paginator(goods,8)
    goods_list = goods_obj.page(page)

    return render(request,'seller/goods.html',locals())

# 修改商品状态
def goods_status(request,id,status):
    goods = Goods.objects.get(id = id)
    if status == 'up':
        goods.goods_status = 1
        goods.save()
    else:
        goods.goods_status = 0
        goods.save()
    url = request.META.get('HTTP_REFERER')
    # return HttpResponseRedirect('/startboot/goods/1/1/')
    return HttpResponseRedirect(url)

# 个人中心
@loginValid
def user_profile(request):
    userid = request.COOKIES.get('userid')
    user = LoginUser.objects.get(id=userid)
    # 处理post请求
    if request.method == 'POST' :
        data = request.POST
        user.email = data.get('email')
        user.username = data.get('username')
        user.phone_number = data.get('phone_number')
        user.age = data.get('age')
        user.gender = data.get('gender')
        user.address = data.get('address')
        if request.FILES.get('img'):
            user.photo = request.FILES.get('img')
        user.save()
    return render(request,'seller/user_profile.html',locals())

# 增加商品类型
def add_label(request):
    GoodsType.objects.create(type_label='新鲜水果',type_description='新鲜水果',type_picture='img/banner01.jpg')
    GoodsType.objects.create(type_label='海鲜水产',type_description='海鲜水产',type_picture='img/banner02.jpg')
    GoodsType.objects.create(type_label='猪牛羊肉',type_description='猪牛羊肉',type_picture='img/banner03.jpg')
    GoodsType.objects.create(type_label='禽类蛋品',type_description='禽类蛋品',type_picture='img/banner04.jpg')
    GoodsType.objects.create(type_label='新鲜蔬菜',type_description='新鲜蔬菜',type_picture='img/banner05.jpg')
    GoodsType.objects.create(type_label='速冻食品',type_description='速冻食品',type_picture='img/banner06.jpg')
    return HttpResponse('添加数据')

# 录入商品
@loginValid
def goods_add(request):
    goods_type = GoodsType.objects.all()
    if request.method == 'POST' :
        user_id = request.COOKIES.get('userid')
        data = request.POST
        goods = Goods()
        goods.goods_number = data.get('goods_number')
        goods.goods_name = data.get('goods_name')
        goods.goods_price = data.get('goods_price')
        goods.goods_count = data.get('goods_count')
        goods.goods_localtion = data.get('goods_localtion')
        goods.goods_safe_date = data.get('goods_safe_date')
        # goods.goods_number = data.get('goods_number')
        goods.goods_type_id = int(data.get('goods_type'))
        goods.goods_store = LoginUser.objects.get(id=user_id)
        goods.goods_picture = request.FILES.get('img')
        goods.save()
    return render(request,'seller/goods_add.html',locals())