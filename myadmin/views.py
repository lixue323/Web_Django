from django.shortcuts import render
from django.core.paginator import Paginator
from . models import users ,types
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
import time,json

def index(request):
	return render(request,'myadmin/index.html')

#用户信息管理
def usersindex(request,pIndex):
	userlist= users.objects.filter()
    #实例化分页对象
	p = Paginator(userlist,5)
    # 处理当前页号信息
	if pIndex=="":
		pIndex = '1'
	pIndex = int(pIndex)
    # 获取当前页数据
	list2 = p.page(pIndex)
	plist = p.page_range
	return render(request,"myadmin/users/usersindex.html",{'users':list2,'pIndex':pIndex,'plist':plist})

def usersadd(request):
	
	return render(request,'myadmin/users/usersadd.html')

def usersinsert(request):
	try:
		a=users()
		a.username=request.GET['nicheng']
		a.name=request.GET['name1']
		import hashlib
		m = hashlib.md5() 
		m.update(bytes(request.GET['passwd'],encoding="utf8"))
		a.passwd = m.hexdigest()
		a.sex=request.GET['sex']
		a.address=request.GET['address']
		a.code=request.GET['code']
		a.phone=request.GET['phone']
		a.email=request.GET['email']
		a.state=request.GET['state']
		a.addtime=time.time()
		a.save()
		context={'info':'添加成功'}
	except:
		context={'info':'添加失败'}
	
	return render(request,'myadmin/info.html' ,context)
	
	

def usersedit(request,uid):
	user1=users.objects.get(id=uid)
	if user1.sex==1:
		a='checked'
		b=None
	elif user1.sex==0:
		a=None
		b='checked'

	if user1.state==0:
		c='checked'
		d=None
		f=None
	elif user1.state==1:
		c=None
		d='checked'
		f=None

	elif user1.state==2:
		c=None
		d=None
		f='checked'

	context={'user':user1,'A':a,'B':b,'C':c,'D':d,'F':f}
	return render(request,'myadmin/users/usersedit.html',context)

def usersupdate(request):
	try:
		a=request.GET['iid']
		b=int(a)
		ob=users.objects.get(id=b)
		ob.username=request.GET['nicheng']
		ob.name=request.GET['name1']
		ob.passwd=request.GET['passwd']
		ob.sex=request.GET['sex']
		ob.code=request.GET['code']
		ob.phone=request.GET['phone']
		ob.email=request.GET['email']
		ob.state=request.GET['state']
		ob.addtime=time.time()
		ob.save()
		context={'info':'修改成功'}
	except:
		context={'info':'修改失败'}
		return render(request,'myadmin/info.html' ,context)


def usersdel(request,uid):
	try:
		a=users.objects.get(id=uid)
		a.delete()
		context={'info':'删除成功'}
	except:
		context={'info':'删除失败'}
	return render(request,'myadmin/info.html',context)

def login(request):
	return render(request,'myadmin/users/login.html')

def dologin(request):
	verifycode = request.session['verifycode']
	code = request.POST['code']
	if verifycode != code:
		context = {'info':'验证码错误！'}
		return render(request,"myadmin/users/login.html",context)
	try:
        #根据账号获取登录者信息
		user = users.objects.get(username=request.POST['username'])
        #判断当前用户是否是后台管理员用户
		if user.state == 0:
            # 验证密码
			import hashlib
			m = hashlib.md5() 
			m.update(bytes(request.POST['passwd'],encoding="utf8"))
			if user.passwd == m.hexdigest():
                # 此处登录成功，将当前登录信息放入到session中，并跳转页面
				request.session['adminuser'] = user.name
                #print(json.dumps(user))
				return redirect(reverse('index'))
			else:
				context = {'info':'登录密码错误！'}
		else:
			context = {'info':'此用户非后台管理用户！'}
	except:
			context = {'info':'登录账号错误！'}
	return render(request,"myadmin/users/login.html",context)

def logout(request):
	del request.session['adminuser']
	return redirect(reverse('login'))
def verify(request):
	  #引入随机函数模块
    import random
    from PIL import Image, ImageDraw, ImageFont
    #定义变量，用于画面的背景色、宽、高
    #bgcolor = (random.randrange(20, 100), random.randrange(
    #    20, 100),100)
    bgcolor = (204,204,204)
    width = 100
    height = 30
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('static/STXIHEI.TTF', 21)
    #font = ImageFont.load_default().font
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, -1), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, -1), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, -1), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, -1), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    """
    python2的为
    # 内存文件操作
    import cStringIO
    buf = cStringIO.StringIO()
    """
    # 内存文件操作-->此方法为python3的
    import io
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')






	
	
	