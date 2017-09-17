from django.shortcuts import render
from django.core.paginator import Paginator
from . models import types,goods,orders,detail,users
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from PIL import Image
import time,json,os

def typeindex(request,pIndex):
	# 执行数据查询，并放置到模板中
    list = types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
    # 遍历查询结果，为每个结果对象追加一个pname属性，目的用于缩进标题
    print(list)
    for ob in list:
        ob.pname ='. . . '*(ob.path.count(',')-1)
        # print(list[0].__dict__)
    context = {"types":list}
    return render(request,'myadmin/type/typeindex.html',context)


def typeadd(request,id1):
	if id1=='0':
		context={'pid':id1,'path':'0,','name':'0'}
	else:
		a=types.objects.get(id=id1)
		context={'pid':str(a.id),'path':a.path+str(a.id)+',' ,'name':a.name}
	return render(request,'myadmin/type/typeadd.html',context)

def typeinsert(request):
	try:
		b=types()
		b.name=request.GET['name1']
		b.pid=request.GET['pid']
		b.path=request.GET['path']
		b.save()
		context={'info':'添加成功'}
	except:
		context={'info':'添加失败'}
	
	return render(request,'myadmin/info.html' ,context)
	
def typedel(request,uid):
	row=types.objects.filter(pid=uid).count()
	print(row)
	if row > 0:
		context={'info':'删除失败:含有子类'}
		return render(request,'myadmin/info.html' ,context)
	
	b=types.objects.get(id=uid)
	b.delete()
	context={'info':'删除成功'}
	
	return render(request,'myadmin/info.html' ,context)
	

def typeedit(request,uid):
	type1=types.objects.get(id=uid)
	context={'type1':type1}
	return render(request,'myadmin/type/typeedit.html',context)

def typeupdate(request):
	try:
		a=request.GET['iid']
		b=int(a)
		ob=types.objects.get(id=b)
		ob.name=request.GET['name1']
		ob.pid=request.GET['grade']
		ob.path=request.GET['path']

		ob.save()
		context={'info':'修改成功'}
	except:
		context={'info':'修改失败'}
	return render(request,'myadmin/info.html' ,context)


#######################################################
#商品信息管理
def goodsindex(request,pIndex):
	a=types.objects.all()
	goodslist= goods.objects.filter()
    #实例化分页对象
	p = Paginator(goodslist,5)
    # 处理当前页号信息
	#if pIndex=="":
	#	pIndex = '1'
	pIndex = int(pIndex)
    # 获取当前页数据
	list2 = p.page(pIndex)
	for i in list2:
		ob=types.objects.get(id=i.typeid)
		i.pname=ob.name
	plist = p.page_range
	return render(request,"myadmin/goods/goodsindex.html",{'goods':list2,'pIndex':pIndex,'plist':plist,'types':a})


def goodsadd(request,gid):
	list = types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
	context={'typelist':list}
	return render(request,'myadmin/goods/goodsadd.html',context)

def goodsinsert(request):
	myfile = request.FILES.get("picname")
	
	if not myfile:
		return HttpResponse("没有上传文件信息！")
    # 以时间戳命名一个新图片名称
	filename= str(time.time())+"."+myfile.name.split('.').pop()
	destination = open(os.path.join("./static/goods/",filename),'wb+')
	for chunk in myfile.chunks():      # 分块写入文件  
		destination.write(chunk)  
	destination.close()

	# 执行图片缩放
	im = Image.open("./static/goods/"+filename)
    # 缩放到375*375:
	im.thumbnail((375, 375))
    # 把缩放后的图像用jpeg格式保存:
	im.save("./static/goods/"+filename, 'jpeg')
    # 缩放到220*220:
	im.thumbnail((220, 220))
    # 把缩放后的图像用jpeg格式保存:
	im.save("./static/goods/m_"+filename, 'jpeg')
    # 缩放到220*220:
	im.thumbnail((100, 100))
    # 把缩放后的图像用jpeg格式保存:
	im.save("./static/goods/s_"+filename, 'jpeg')


	try:
		b=goods()
		b.typeid=request.POST['typeid']
		b.goods=request.POST['goods']
		b.company=request.POST['company']
		b.desc=request.POST['desc']
		b.price=request.POST['price']
		b.picname=filename
		b.state= 1
		b.store=request.POST['store']
		b.addtime=time.time()
		b.save()
		context={'info':'添加成功'}
	except:
		context={'info':'添加失败'}
	return render(request,'myadmin/info.html' ,context)

def goodsdel(request,gid):
	try:
		a=goods.objects.get(id=gid)
		os.remove("./static/goods/"+a.picname)   
		os.remove("./static/goods/m_"+a.picname)   
		os.remove("./static/goods/s_"+a.picname)
		a.delete()
		context={'info':'删除成功'}

	except:
		context={'info':'删除失败'}
	return render(request,'myadmin/info.html' ,context)

def goodsedit(request,gid):

	list = types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')

	a=goods.objects.get(id=gid)

	context={'goods':a,'typelist':list}
	return render(request,'myadmin/goods/goodsedit.html',context)
	
def goodsupdate(request):
	a=request.POST['ggid']
	d=int(a)

	try:
		b = False
		oldpicname = request.POST['oldpicname']
		if None != request.FILES.get("picname"):
			myfile = request.FILES.get("picname", None)
			if not myfile:
				return HttpResponse("没有上传文件信息！")
            # 以时间戳命名一个新图片名称
			filename = str(time.time())+"."+myfile.name.split('.').pop()
			destination = open(os.path.join("./static/goods/",filename),'wb+')
			for chunk in myfile.chunks():      # 分块写入文件  
				destination.write(chunk)  
			destination.close()
            # 执行图片缩放
			im = Image.open("./static/goods/"+filename)
            # 缩放到375*375:
			im.thumbnail((375, 375))
            # 把缩放后的图像用jpeg格式保存:
			im.save("./static/goods/"+filename, 'jpeg')
            # 缩放到220*220:
			im.thumbnail((220, 220))
            # 把缩放后的图像用jpeg格式保存:
			im.save("./static/goods/m_"+filename, 'jpeg')
            # 缩放到220*220:
			im.thumbnail((100, 100))
            # 把缩放后的图像用jpeg格式保存:
			im.save("./static/goods/s_"+filename, 'jpeg')
			b = True
			picname = filename
		else:
			picname = oldpicname
		ob = goods.objects.get(id=d)
		ob.goods = request.POST['goods']
		ob.typeid = request.POST['typeid']
		ob.company = request.POST['company']
		ob.price = request.POST['price']
		ob.store = request.POST['store']
		ob.desc = request.POST['desc']
		ob.picname = picname
		ob.state = request.POST['state']
		ob.save()
		context = {'info':'修改成功！'}
		if b:
			os.remove("./static/goods/m_"+oldpicname) #执行老图片删除  
			os.remove("./static/goods/s_"+oldpicname) #执行老图片删除  
			os.remove("./static/goods/"+oldpicname) #执行老图片删除  
	except:
		context = {'info':'修改失败！'}
		if b:
			os.remove("./static/goods/m_"+picname) #执行新图片删除  
			os.remove("./static/goods/s_"+picname) #执行新图片删除  
			os.remove("./static/goods/"+picname) #执行新图片删除  
	return render(request,"myadmin/info.html",context)







	myfile = request.FILES.get("picname")

    # 以时间戳命名一个新图片名称
	filename= str(time.time())+"."+myfile.name.split('.').pop()
	print(filename)
	destination = open(os.path.join("./static/goods/",filename),'wb+')
	for chunk in myfile.chunks():      # 分块写入文件  
		destination.write(chunk)  
	destination.close()

	# 执行图片缩放
	im = Image.open("./static/goods/"+filename)
    # 缩放到375*375:
	im.thumbnail((375, 375))
    # 把缩放后的图像用jpeg格式保存:
	im.save("./static/goods/"+filename, 'jpeg')
    # 缩放到220*220:
	im.thumbnail((220, 220))
    # 把缩放后的图像用jpeg格式保存:
	im.save("./static/goods/m_"+filename, 'jpeg')
    # 缩放到220*220:
	im.thumbnail((100, 100))
    # 把缩放后的图像用jpeg格式保存:
	im.save("./static/goods/s_"+filename, 'jpeg')

	try:
		a=request.POST['ggid']
		d=int(a)
		b=goods.objects.get(id=d)

		b.typeid=request.POST['typeid']
		b.goods=request.POST['goods']
		b.company=request.POST['company']
		b.desc=request.POST['desc']
		b.price=request.POST['price']
		b.picname=filename
		b.state=request.POST['state']
		b.store=request.POST['store']
		b.num=request.POST['num']
		b.clicknum=request.POST['clicknum']
		b.addtime=request.POST['addtime']
		b.save()
		context={'info':'修改成功'}
	except:
		context={'info':'修改失败'}
	return render(request,'myadmin/info.html' ,context)
	


#######################################################
#商品订单管理

def ordersindex(request,pIndex):
	a=request.session['webuser']['name']
	
	a=orders.objects.all()
	orderslist= orders.objects.filter()
    #实例化分页对象
	p = Paginator(orderslist,5)
    # 处理当前页号信息
	#if pIndex=="":
	#	pIndex = '1'
	pIndex = int(pIndex)
    # 获取当前页数据
	list2 = p.page(pIndex)
	#for i in list2:
	#	ob=types.objects.get(id=i.typeid)
	#	i.pname=ob.name
	plist = p.page_range
	for i in list2:
		ob=users.objects.get(id=i.uid)
		i.pname=ob.name
	return render(request,"myadmin/orders/ordersindex.html",{'orders':list2,'pIndex':pIndex,'plist':plist,'a':a})

def detail1(request,oid):
	detaillist=detail.objects.filter(orderid=oid)
	context={'detaillist':detaillist}
	return render(request,'myadmin/orders/detail.html',context)

def ordersedit(request,oid):
	orderclick=orders.objects.get(id=oid)
	context={'orderclick':orderclick}
	return render(request,'myadmin/orders/ordersedit.html',context)

def orderschange(request):
	try:
		a=request.GET['ggid']
		b=int(a)
		ob=orders.objects.get(id=b)
		
		ob.status=request.GET['state']
	

		ob.save()
		context={'info':'修改成功'}
	except:
		context={'info':'修改失败'}
	return render(request,'myadmin/info.html' ,context)