from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from . models import users,types,goods
import time
# Create your views here.

def loadContext(request):
    context={}
    context['typelist'] = types.objects.filter(pid=0)
    return context

def myweb_index(request):
	return render(request,'shop/index.html')


def show(request,tid=0):
    context = loadContext(request)
    # 获取所需商品列表信息并放置到context
    if tid == 0:
    	# return HttpResponse(request.GET.get('ttid',None))
    	context['goodslist'] = goods.objects.all()
    else:
    	ob = types.objects.get(id=tid)
    	context['types'] = types.objects.filter(pid=tid)
    	context['types1'] = types.objects.filter(id=tid)
    	if (tid) and (ob.pid != 0):
    		context['goodslist']=goods.objects.filter(typeid=tid)
    	else:
    		context['goodslist'] = goods.objects.filter(typeid__in=types.objects.only('id').filter(path__contains=','+str(tid)+','))
    return render(request,'shop/show.html',context)
def content(request):
	return render(request,'shop/content.html')

def buycar(request):
	return render(request,'shop/buycar.html')

def myweb_add(request):
	try:
		a=users()
		a.username=request.GET['username']
		a.name=request.GET['name']
		import hashlib
		m = hashlib.md5() 
		m.update(bytes(request.GET['passwd'],encoding="utf8"))
		a.passwd = m.hexdigest()
		a.sex=request.GET['sex']
		a.code=request.GET['code']
		a.phone=request.GET['phone']
		a.email=request.GET['email']
		a.state=1
		a.addtime=time.time()
		a.save()
		context={'logininfo':'注册成功'}
	except:
		context={'logininfo':'注册失败'}
	
	return render(request,'shop/logininfo.html' ,context)

def myweb_login(request):
	return render(request,'shop/denglu1.html')

def myweb_dologin(request):
	verifycode = request.session['verifycode']
	code = request.POST['code']
	if verifycode != code:
		context = {'info':'验证码错误！'}
		return render(request,"shop/denglu1.html",context)
	try:
        #根据账号获取登录者信息
		user = users.objects.get(username=request.POST['username'])
        #判断当前用户是否是后台管理员用户
		if user.state == 1 or user.state == 0:
            # 验证密码
			import hashlib
			m = hashlib.md5() 
			m.update(bytes(request.POST['passwd'],encoding="utf8"))
			if user.passwd == m.hexdigest():
                # 此处登录成功，将当前登录信息放入到session中，并跳转页面
				request.session['webuser'] = user.name
                #print(json.dumps(user))
				return redirect(reverse('myweb_index'))
			else:
				context = {'info':'登录密码错误！'}
		else:
			context = {'info':'此用户非注册用户！'}
	except:
			context = {'info':'登录账号错误！'}
	return render(request,"shop/denglu1.html",context)

def myweb_logout(request):
	del request.session['webuser']
	return redirect(reverse('myweb_index'))
def myweb_verify(request):
	  #引入随机函数模块
    import random
    from PIL import Image, ImageDraw, ImageFont
    #定义变量，用于画面的背景色、宽、高
    #bgcolor = (random.randrange(20, 100), random.randrange(
    #    20, 100),100)
    bgcolor = (204,204,204)
    width = 120
    height = 50
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
    fontcolor = (248,115,0)
    #绘制4个字
    draw.text((5, 3), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 3), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 3), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 3), rand_str[3], font=font, fill=fontcolor)
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
