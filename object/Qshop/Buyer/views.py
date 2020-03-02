from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
import hashlib
from Seller.models import *
from .models import *
from django.core.paginator import Paginator

# Create your views here.

# 退出
def logout(request):
    response = HttpResponseRedirect('/login/')
    response.delete_cookie('buy_email')
    response.delete_cookie('buy_username')
    response.delete_cookie('buy_userid')
    del request.session['buy_email']
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
        cookie_email = request.COOKIES.get('buy_email')
        session_email = request.session.get('buy_email')
        if cookie_email and session_email and cookie_email == session_email:
            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/login/')
    return inner

# 首页
def index(request):
    goods_type = GoodsType.objects.all()
    res = []
    for one in goods_type :
        goods = one.goods_set.order_by('id').all()
        if len(goods) > 4 :
            goods_list = goods[:4]
            res.append({'type':one,'goods_list':goods_list})
        elif len(goods) > 0 and len(goods) <= 4:
            goods_list = goods
            res.append({'type': one, 'goods_list': goods_list})
    return render(request,'buyer/index.html',locals())

# 登录
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        if username and password:
            user = LoginUser.objects.filter(username=username, user_type=1,password=setPassword(password)).first()
            if user:
                response = HttpResponseRedirect('/')
                response.set_cookie('buy_email', user.email)
                response.set_cookie('buy_username', user.username)
                response.set_cookie('buy_userid', user.id)
                request.session['buy_email'] = user.email
                return response
            else:
                message = '账号密码不正确'
        else:
            message = '参数为空'
    return render(request,'buyer/login.html',locals())

# 注册
def register(request):
    # 接受参数
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        repassword = request.POST.get('cpwd')
        email = request.POST.get('email')
        # 校验数据
        if email and password and password == repassword:
            LoginUser.objects.create(email=email, username=username,password=setPassword(password),user_type=1)
            return HttpResponseRedirect('/login/')
        else:
            megass = '输入错误'
    return render(request,'buyer/register.html',locals())

# 商品列表页面
def goods_list(request,page=1):
    kywards = request.GET.get('kywards')
    req_type = request.GET.get('req_type')

    if req_type == 'find_all':
        goods_type = GoodsType.objects.filter(id = kywards).first()
        goods = goods_type.goods_set.order_by('-goods_pro_time')
    else:
        goods = Goods.objects.filter(goods_name__contains=kywards).order_by('-goods_pro_time')
        # goods_new = goods[:2]
    goods_new = goods[:2]
    # pagnitor_obj = Paginator(goods,6)
    # page_obj = pagnitor_obj.page(page)
    return render(request,'buyer/list.html',locals())

#商品详情页
def goods_detail(request):
    goods_id = request.GET.get('goods_id')
    goods = Goods.objects.get(id=goods_id)
    goods_new = Goods.objects.filter(goods_type=goods.goods_type).order_by('-goods_pro_time')[:2]
    return render(request,'buyer/detail.html',locals())

# uuid
def get_order_no():
    import uuid
    order_no = str(uuid.uuid4())
    return order_no

# 订单页面
@loginValid
def goods_place_order(request):
    user_id = request.COOKIES.get('buy_userid')
    goods_id = request.GET.get('goods_id')
    goods_count = int(request.GET.get('goods_count'))

    goods = Goods.objects.get(id = goods_id)

    payorder = PayOrder()
    payorder.order_number = get_order_no()
    payorder.order_status = 1
    payorder.order_total = goods_count * goods.goods_price
    payorder.order_user_id = int(user_id)
    payorder.save()

    order_info = OrderInfo()
    order_info.order = payorder
    order_info.goods = goods
    order_info.goods_price = goods.goods_price

    order_info.store = goods.goods_store
    order_info.goods_count = goods_count
    order_info.goods_total_price = goods_count * goods.goods_price
    order_info.save()
    return render(request,'buyer/place_order.html',locals())

# 订单详情页面



