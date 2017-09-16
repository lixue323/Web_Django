from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from . models import users,types,goods,orders,detail
import time,json
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
def content(request,tid):

    a=goods.objects.get(id=tid)
    types1=types.objects.get(id=a.typeid)
    context={'goods':a,'types1':types1}
    return render(request,'shop/content.html',context)

def contentbuy(request,tid):
    
    goods1 = goods.objects.get(id=tid)
    shop = goods1.toDict();
   
    #从session获取购物车信息
    if 'shoplist' in request.session:
        shoplist = request.session['shoplist']
    else:
        shoplist = {}
   
    shoplist[tid]=shop

    #将购物车信息放回到session
    request.session['shoplist'] = shoplist
    return redirect(reverse('buycar'))

def myweb_orderlist(request):
    ids = request.GET['gids']
    if ids == '':
        return HttpResponse("购物车无商品")
    gids = ids.split(',')

    shoplist = request.session['shoplist']

    orderlist = {}
    total = 0
    for sid in gids:
        orderlist[sid] = shoplist[sid]
        total+=shoplist[sid]['price']
    print(total)
    request.session['orderlist'] = orderlist
    request.session['total'] = total
    
    return render(request,"shop/orderlist.html")
def myweb_orderconfirm(request):
    return render(request,"shop/orderconfirm.html")

def myweb_orderinsert(request):
    # 封装订单信息，并执行添加
    orders1 = orders()
    orders1.uid = request.session['webuser']['id']
    orders1.linkman = request.POST['linkman']
    orders1.address = request.POST['address']
    orders1.code = request.POST['code']
    orders1.phone = request.POST['phone']
    orders1.addtime = time.time()
    orders1.total = request.session['total']
    orders1.status = 0
    orders1.save()
    #获取订单详情
    orderlist = request.session['orderlist']
    #遍历购物信息，并添加订单详情信息
    for shop in orderlist.values():
        print(shop)
        detail2 = detail()
        detail2.orderid = orders1.id
        detail2.goodid = shop['id']
        detail2.name = shop['goods']
        detail2.price = shop['price']
        #detail2.num = shop['m']
        detail2.save()
    return HttpResponse("订单成功：订单id号："+str(orders1.id))


def buycar(request):
    return render(request,'shop/buycar.html')

def buycardel(request,tid):
    shoplist = request.session['shoplist']
    del shoplist[tid]
    request.session['shoplist'] = shoplist
    return redirect(reverse('buycar'))
    
def buycarclear(request):
    context = loadContext(request)
    request.session['shoplist'] = {}
    return render(request,"shop/buycar.html",context)
    
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
                request.session['webuser'] = user.toDict()
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



