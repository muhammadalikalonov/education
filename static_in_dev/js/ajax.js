    $(function () {
        $('#search').keyup(function () {
            let data = {
                'search_text': $(this).val(),
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            }
            $.ajax({
                method: 'GET',
                url: "/search/",
                data: data,

            }).done(e => {
                $('#filteredUni').html(e.data);
                $('#filteredUni').ready(function(){
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
                });
            });

        });

        

    });

function searchSuccess(data, textStatus, jqXHR) {
    // console.log(data)
    $('#filteredUni').html(data.data);
}