$(document).ready(function(){
	$(".ajaxLoader").hide();
 $(".checkbox__input").on('click',function(){
		var _filterObj={};
		// var _minPrice=$('#maxPrice').attr('min');
		// var _maxPrice=$('#maxPrice').val();
		// _filterObj.minPrice=_minPrice;
		// _filterObj.maxPrice=_maxPrice;
		$(".checkbox__input").each(function(index,ele){
			var _filterVal=$(this).val();
			var _filterKey=$(this).data('filter');
			_filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
			 	return el.value;
			});
		});
		// console.log(_filterObj);

		// Run Ajax
		$.ajax({
			url:'/filter',
			data:_filterObj,
			dataType:'json',
			beforeSend:function(){
			    // $("#filteredUni ").html('loading');
				$(".ajaxLoader").show();
			},
			success:function(res){
				console.log(res);
				$("#filteredUni ").html(res.univer);
				$(".ajaxLoader").hide();
                    if (document.querySelector('.card-tmp__slider')) {
                        let sliders_st = document.querySelectorAll('.card-tmp__slider');
                        sliders_st.forEach(el => {
                            new Swiper(el, {
                                slidesPerView: 1,
                                observer: true,
                                observeParents: true,
                                autoHeight: false,
                                speed: 500,
                                spaceBetween: 10,
                                simulateTouch: true,
                                navigation: {
                                    nextEl: el.parentElement.querySelector('.card-tmp__slider-btn_next'),
                                    prevEl: el.parentElement.querySelector('.card-tmp__slider-btn_prev'),
                                },
                            });
                        });
                    }
			}
		});
	});
	// End

	// // Filter Product According to the price
	// $("#maxPrice").on('blur',function(){
	// 	var _min=$(this).attr('min');
	// 	var _max=$(this).attr('max');
	// 	var _value=$(this).val();
	// 	console.log(_value,_min,_max);
	// 	if(_value < parseInt(_min) || _value > parseInt(_max)){
	// 		alert('Values should be '+_min+'-'+_max);
	// 		$(this).val(_min);
	// 		$(this).focus();
	// 		$("#rangeInput").val(_min);
	// 		return false;
	// 	}
	// });

	// $("#priceFilterBtn").on('click',function(){
	// 	var _minPrice=$(this).data('min');
	// 	var _maxPrice=$('#maxPrice').val();
	// 	var _filterObj={};
	// 	$(".filter-checkbox").each(function(index,ele){
	// 		var _filterVal=$(this).val();
	// 		var _filterKey=$(this).data('filter');
	// 		_filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
	// 		 	return el.value;
	// 		});
	// 	});
	// 	_filterObj.minPrice=_minPrice;
	// 	_filterObj.maxPrice=_maxPrice;
	// 	// Run Ajax
	// 	$.ajax({
	// 		url:'/filter-data',
	// 		data:_filterObj,
	// 		dataType:'json',
	// 		beforeSend:function(){
	// 			$(".ajaxLoader").show();
	// 		},
	// 		success:function(res){
	// 			console.log(res);
	// 			$("#filteredProducts").html(res.data);
	// 			$(".ajaxLoader").hide();
	// 		}
	// 	});
	// });
	// End
	// if(window.location.pathname.charAt(1) == 'r'){
	// 	$('lang__item-ru').addClass('_active')
	// }else{
	// 	$('lang__item-uz').addClass('_active')
	// }

});

// document.getElementById('zor').addEventListener('click', function () {
// 		let heroTxtTimer = document.getElementById('hero_txt_timer');
// 			function removeLoader() {
// 				heroTxtTimer.style.display = 'none';
// 			}
// 			setInterval (removeLoader, 500)
// 			console.log(heroTxtTimer)
// 			console.log('jjh')
//
// })
