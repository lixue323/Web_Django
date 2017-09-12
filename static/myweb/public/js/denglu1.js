$('.options li').click(function(){
	//当前点击的元素添加class 其它同步移出class
	$(this).addClass('active').siblings().removeClass('active');
	//获取当前点击元素的索引
	var v = $(this).index();
	$('.card li').eq(v).removeClass('active').siblings().addClass('active');
})



//声明全局变量
var NameOk = false;
var PassOk = false;
var EmailOk = false;
var PhoneOk = false;

$('input').focus(function(){
	
	$(this).css('border','1px solid blue');
})

// 验证昵称
$('input[name=username]').blur(function(){
	//获取用户的输入信息
	var v = $(this).val();
	var reg = /^\w{6,8}$/;
	if(reg.test(v)){
		$(this).next('span').html('√').css('color','white');
		$(this).css('border','2px solid green');
		//修改全局变量
		NameOk = true;
	}else{
		$(this).next('span').html('×').css('color','red');
		$(this).css('border','2px solid red');
		//修改全局变量
		NameOk = false;
	}
})


// 验证密码
$('input[name=passwd]').blur(function(){
	//获取用户的输入信息
	var v = $(this).val();
	var reg = /^\w{6,18}$/;
	if(reg.test(v)){
		$(this).next('span').html('√').css('color','white');
		$(this).css('border','2px solid green');
		//修改全局变量
		PassOk = true;
	}else{
		$(this).next('span').html('×').css('color','red');
		$(this).css('border','2px solid red');
			//修改全局变量
		PassOk = false;
	}
})

// 验证邮箱
$('input[name=email]').blur(function(){
	//获取用户的输入信息
	var v = $(this).val();
	var reg = /^\w+@\w+\.(com|cn|org|net)$/;
	if(reg.test(v)){
		$(this).next('span').html('√').css('color','white');
		$(this).css('border','2px solid green');
		//修改全局变量
		EmailOk = true;
	}else{
		$(this).next('span').html('×').css('color','red');
		$(this).css('border','2px solid red');
		//修改全局变量
		EmailOk = false;
	}
})

// 验证电话
$('input[name=phone]').blur(function(){
	//获取用户的输入信息
	var v = $(this).val();
	var reg = /^\d{11}$/;
	if(reg.test(v)){
		$(this).next('span').html('√').css('color','white');
		$(this).css('border','2px solid green');
		//修改全局变量
		PhoneOk = true;
	}else{
		$(this).next('span').html('×').css('color','red');
		$(this).css('border','2px solid red');
		//修改全局变量
		PhoneOk = false;
	}
})

//表单提交事件 submit
$('#b').submit(function(){
	//触发input 丧失焦点事件
	$('#b input').trigger('blur');

	//判断如果都正确
	if(NameOk && PassOk){
		return true;
	}

	//阻止默认行为
	return false;
})

$('#b1').submit(function(){
	//触发input 丧失焦点事件
	$('#b1 input').trigger('blur');

	//判断如果都正确
	if(NameOk && PassOk && PhoneOk &&EmailOk){
		return true;
	}
	
	//阻止默认行为
	return false;
})

