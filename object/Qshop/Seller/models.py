from django.db import models

# Create your models here.
GENDER_STATUS = (
    (0,'女'),
    (1,'男'),
)


class LoginUser(models.Model):
    email = models.EmailField(verbose_name='邮箱')
    password = models.CharField(max_length=32,verbose_name='密码')
    phone_number = models.CharField(max_length=11,verbose_name='手机号',null=True,blank=True)
    age = models.IntegerField(verbose_name='年龄',null=True,blank=True)
    gender = models.IntegerField(choices=GENDER_STATUS,verbose_name='性别',default=1)
    address = models.TextField(verbose_name='地址',null=True,blank=True)
    photo = models.ImageField(upload_to='img',default='img/timg01.jpg',verbose_name='头像')
    username = models.CharField(max_length=32,verbose_name='用户名',default='')
    user_type = models.IntegerField(default=1,verbose_name='用户身份') #0卖家  #1买家
    class Meta:
        db_table = 'loginuser'

class GoodsType(models.Model):
    type_label = models.CharField(max_length=32,verbose_name='类型标签')
    type_description = models.TextField(verbose_name='类型的描述')
    type_picture = models.ImageField(max_length=64,verbose_name='类型的图片')
    class Meta:
        db_table = 'goods_type'

class Goods(models.Model):
    goods_number = models.CharField(max_length=11,verbose_name='商品编号')
    goods_name = models.CharField(max_length=32,verbose_name='商品名字')
    goods_price = models.FloatField(verbose_name='商品价格')
    goods_count = models.IntegerField(verbose_name='商品数量')
    goods_localtion = models.CharField(max_length=32,verbose_name='商品产地')
    goods_safe_date = models.IntegerField(verbose_name='商品保质期')
    goods_pro_time = models.DateTimeField(auto_now=True,verbose_name='生成日期')
    goods_status = models.IntegerField(verbose_name='商品状态',default=1) ## 0上架  1下架
    goods_picture = models.ImageField(default='img/timg01.jpg',upload_to='img',verbose_name='商品的图片')
    goods_description = models.TextField(default='好吃',verbose_name='商品的描述')
    goods_type = models.ForeignKey(to=GoodsType,on_delete=models.CASCADE)
    goods_store = models.ForeignKey(to=LoginUser,on_delete=models.CASCADE)
    class Meta:
        db_table = 'goods'
