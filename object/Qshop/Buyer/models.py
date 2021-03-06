from django.db import models
from Seller.models import *

# Create your models here.

ORDER_STATUS = (
    (1,'未支付'),
    (2,'已支付'),
    (3,'待发货'),
    (4,'已发货'),
    (5,'拒收'),
    (6,'已完成'),
)

class PayOrder(models.Model):
    order_number = models.CharField(max_length=64,unique=True,verbose_name='订单号')
    order_date = models.DateField(auto_now=True,verbose_name='订单创建的时间')
    order_status = models.IntegerField(choices=ORDER_STATUS,verbose_name='订单的状态')
    order_total = models.FloatField(verbose_name='订单的总价')
    order_user = models.ForeignKey(to=LoginUser,on_delete=models.CASCADE,verbose_name='买家')
    class Meta:
        db_table = 'pay_order'

class OrderInfo(models.Model):
    order = models.ForeignKey(to=PayOrder,on_delete=models.CASCADE)
    goods = models.ForeignKey(to=Goods,on_delete=models.CASCADE)
    goods_price = models.FloatField(verbose_name='商品的单价')
    store = models.ForeignKey(to=LoginUser,on_delete=models.CASCADE,verbose_name='卖家')
    goods_count = models.IntegerField(verbose_name='购买商品的数量')
    goods_total_price = models.FloatField(verbose_name='购买商品的总金额')
    class Meta:
        db_table = 'order_info'
