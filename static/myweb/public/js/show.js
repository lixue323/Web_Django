 //导航栏下方选择区鼠标移入移出效果
	$('.select2 li').mouseover(function(){
		$(this).css({color:'orange',cursor:'pointer'})

	})


	$('.select2 li').mouseout(function(){
		$(this).css({color:'#333333',cursor:'default'})

	})
 //end 导航栏下方选择区鼠标移入移出效果


    
 //鼠标移入移出图片效果
 $('.thumbnail img').mouseover(function(){
 	$(this).css('border','5px solid orange')

 })

  $('.thumbnail img').mouseout(function(){
 	$(this).css('border','none')
 })

 //end鼠标移入移出图片效果
 