
$(document).ready(function () {
    var _filterObj = {};
    $(".ajaxLoader").hide();

    function getParameterByName(name, url = window.location.href) {
        name = name.replace(/[\[\]]/g, '\\$&');

        var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
            results = regex.exec(url);
        if (!results) return null;
        if (!results[2]) return '';
        return decodeURIComponent(results[2].replace(/\+/g, ' '));
    }

    $('[data-filter="country"]').each((e, val) => {
        if (val.value === getParameterByName('country', window.location.href)) {
            val.checked = true
            _filterObj.country = [val.value]


        }
    })


    ajaxFilter()
    $('[data-filter="sorting"]').on('click', function () {
        let _name = $(this)[0].name
        _filterObj.maxPrice = false
        _filterObj.minPrice = false
        _filterObj.popPrice = false
        _filterObj[_name] = _filterObj[_name] ? !_filterObj[_name] : true
        ajaxFilter()
    })
    $('#search').keyup(function () {
        _filterObj.search_text = $(this).val()
        ajaxFilter()
    });
    $(".checkbox__input").on('click', function () {

        $(".checkbox__input").each(function (index, ele) {
            var _filterVal = $(this).val();
            var _filterKey = $(this).data('filter');
            _filterObj[_filterKey] = Array.from(document.querySelectorAll('input[data-filter=' + _filterKey + ']:checked')).map(function (el) {
                return el.value;
            });
        });
        ajaxFilter()
    });

    function ajaxFilter() {

        $.ajax({
            url: '/filter',
            data: _filterObj,
            dataType: 'json',
            beforeSend: function () {
                // $("#filteredUni ").html('loading');
                $(".ajaxLoader").show();
            },
            success: function (res) {
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
    }


});