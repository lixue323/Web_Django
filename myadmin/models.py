from django.db import models

# Create your models here.
class users(models.Model):
	username=models.CharField(max_length=32)
	name=models.CharField(max_length=16)
	passwd=models.CharField(max_length=32)
	sex=models.IntegerField(1)
	address=models.TextField(255)
	code=models.CharField(max_length=6)
	phone=models.CharField(max_length=16)
	email=models.CharField(max_length=50)
	state=models.IntegerField(1)
	addtime=models.IntegerField(11)

	class Meta:
		db_table='myweb_users'
#商品类型
class types(models.Model):
	name=models.CharField(max_length=32)
	pid=models.IntegerField(11)
	path=models.CharField(max_length=255)
	

	class Meta:
		db_table='myweb_types'


#商品信息
class goods(models.Model):
	typeid=models.IntegerField(11)
	goods=models.CharField(max_length=32)
	company=models.CharField(max_length=50)
	desc=models.TextField()
	price=models.FloatField()
	picname=models.CharField(max_length=255)
	state=models.IntegerField(1)
	store=models.IntegerField(11)
	num=models.IntegerField(11)
	clicknum=models.IntegerField(11)
	addtime=models.IntegerField(11)

	class Meta:
		db_table='myweb_goods'

class orders(models.Model):
    uid = models.IntegerField()
    linkman = models.CharField(max_length=32)
    adress = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    addtime = models.IntegerField()
    total = models.FloatField()
    status = models.IntegerField()

    class Meta:
    	db_table='myweb_orders'



class detail(models.Model):
    orderid = models.IntegerField()
    goodid = models.IntegerField()
    name = models.CharField(max_length=32)
    price = models.FloatField()
    num = models.IntegerField()

    class Meta:
    	db_table='myweb_detail'