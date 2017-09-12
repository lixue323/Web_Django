	
	 // 轮播图左侧鼠标移入移出的效果
	$('.head2 li').mouseover(function(){
	$(this).addClass('head3');
	var v = $(this).index();
	$('#head4').show()
	$('.card li').eq(v).show();
	})


	$('.head2 li').mouseout(function(){
		$(this).removeClass('head3')
		var v = $(this).index();
		$('head4').hide();
		$('.card li').eq(v).hide();
		
	})



	
 //  end 轮播图左侧鼠标移入移出的效果

 //导航栏下方选择区鼠标移入移出效果
	$('.select2 li').mouseover(function(){
		$(this).css({color:'orange',cursor:'pointer'})

	})


	$('.select2 li').mouseout(function(){
		$(this).css({color:'#333333',cursor:'default'})

	})
 //end 导航栏下方选择区鼠标移入移出效果

 //设置热门商品展示栏定时动画
    setInterval(function(){
 	   $('#goods').slideUp()
     },3000)

    setInterval(function(){
 	   $('#goods1').slideDown()
     },3000)

     setInterval(function(){
 	   $('#goods1').slideUp()
     },5000)

     setInterval(function(){
 	   $('#goods').slideDown()
     },5000)


    
 // end设置热门商品展示栏定时动画
    
 //鼠标移入移出图片效果
 $('.good img').mouseover(function(e){
 	$(this).css('border','3px dotted orange')
 	

 })

  $('.good img').mouseout(function(){
 	$(this).css('border','none')
 
 })

 //end鼠标移入移出图片效果