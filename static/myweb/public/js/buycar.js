		//封装函数 (计算总价)
		function allMoney(){
				//获取每样商品的总计价格
			 	var one= Number($('.prices').eq(0).text())
			 	var two= Number($('.prices').eq(1).text())
			 	var three= Number($('.prices').eq(2).text())
			 	var four= Number($('.prices').eq(3).text())
			 	//设置购物车里所有商品的价格
			 	$('#allprices').text(one+two+three+four)

		}
		allMoney()

		//封装函数 统计当前商品的数量
		function allN(){

		var allNum=$('.chk').length
		
		$('#allgoodsnum').text(allNum)
		}

		allN()


		//封装函数 获取选中商品的数量(没成功,功能有待提升)
		/*function chkAll(){
			var chk = document.getElementsByClassName('chk');
			var n=$('input[checked]').length
		
			$('#chkgoodsnum').text(n)
		}	

		chkAll()
*/


		

		// 实现全选框的功能
		var chkall=true;
		$(function(){
		       $('#checkall').click(function(){
		       $(".chk").prop("checked",chkall);
		       chkall=!chkall  
		    })

		})


		//实现商品加减,以及总共价格的变化
			
		var b=0;
		$('.jia').click(function(){
			var number=$(this).parents('td').find('input').val();

			var a=Number(number)+1;
			b=String(a);
			$(this).parents('td').find('input').val(b)
			var dj=$(this).parents('tr').find('td').eq(2).text()
			var z=Number(dj)
		
			$(this).parents('tr').find('td').eq(4).text(z*a)

			allMoney()
	
		})


		$('.jian').click(function(){
			var number=$(this).parents('td').find('input').val();

			var a=Number(number)-1;
			if(a>=1){
			b=String(a);
			$(this).parents('td').find('input').val(b)
			var dj=$(this).parents('tr').find('td').eq(2).text()
			var z=Number(dj)
			$(this).parents('tr').find('td').eq(4).text(z*a)
			
			$(this).parents('tr').find('td').eq(4).text(z*a)
		}else{
			$(this).parents('td').find('input').val(1)
		}
			
			allMoney()

		})		

		

		//实现商品的删除功能
			$('.remov').click(function(){
				$(this).parents('tr').remove()
				allN()
				allMoney()			
			})
