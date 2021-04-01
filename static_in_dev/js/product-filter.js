// $(document).ready(function () {
//     let filter_list = new Map()
//
//     let arrayCountry = new Map()
//     let arrayStudy = new Map()
//     let arrayFaculty = new Map()
//
//     // $(".ajaxLoader").hide();
//     $("[data-filter]").on('click', function () {
//         let arrayHistory = {}
//
//         if ($(this).data('filter') === 'country') {
//             let parent = $(this).parents('.uni__filters-soller-drop')
//             let checked = parent.find('[data-filter]')
//             for (let i = 0; i < checked.length; i++) {
//                 if (checked[i].checked) arrayCountry.set(i, checked[i].value)
//                 else arrayCountry.delete(i)
//             }
//         }
//         if ($(this).data('filter') === 'study') {
//             let parent = $(this).parents('.uni__filters-soller-drop')
//             let checked = parent.find('[data-filter]')
//             for (let i = 0; i < checked.length; i++) {
//                 if (checked[i].checked) arrayStudy.set(i, checked[i].value)
//                 else arrayStudy.delete(i)
//             }
//         }
//         if ($(this).data('filter') === 'faculty') {
//             let parent = $(this).parents('.uni__filters-soller-drop')
//             let checked = parent.find('[data-filter]')
//             for (let i = 0; i < checked.length; i++) {
//                 if (checked[i].checked) arrayFaculty.set(i, checked[i].value)
//                 else arrayFaculty.delete(i)
//             }
//         }
//
//         if (arrayCountry.size) {
//
//             let array = []
//             arrayCountry.forEach(function (value, key) {
//                 array.push(value)
//             });
//             filter_list.set('country', array.toLocaleString())
//         }else{
//             filter_list.delete('country')
//         }
//         if (arrayStudy.size) {
//             let array = []
//             arrayStudy.forEach(function (value, key) {
//                 array.push(value)
//             });
//             filter_list.set('study', array.toLocaleString())
//             // history.replaceState(null, null, "?"+this.serialize(array));
//         }else{
//             filter_list.delete('study')
//         }
//         if (arrayFaculty.size) {
//             let array = []
//             arrayFaculty.forEach(function (value, key) {
//                 array.push(value)
//             });
//             filter_list.set('faculty', array.toLocaleString())
//         }else{
//             filter_list.delete('faculty')
//         }
//         for (let [key, value] of filter_list.entries()) {
//             arrayHistory[key] = value
//         }
//         history.replaceState(null, null, "?" + serialize(arrayHistory));
//         let queryParams = "?" + serialize(arrayHistory)
//
//         // console.log(filter_list)
//         // console.log(serialize(arrayHistory))
//
//         // $(".checkbox__input").each(function(index,ele){
//         // 	var _filterVal=$(this).val();
//         // 	var _filterKey=$(this).data('filter');
//         // 	_filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
//         // 	 	return el.value;
//         // 	});
//         // });
//         //
//         // // Run Ajax
//         fetch(`/contact/filter/`,queryParams )
//         // $.ajax({
//         // 	url: 'filter_data',
//         // 	data:_filterObj,
//         // 	dataType:'json',
//         // 	beforeSend:function(){
//         // 	    // $(".ajaxLoader").html('loading');
//         //
//         // 		$(".ajaxLoader").show();
//         // 	},
//         // 	success:function(res){
//         // 		console.log(res);
//         // 		// $(".ajaxLoader").html(res.data);
//         // 		$(".ajaxLoader").hide();
//         // 	}
//         // });
//     });
//
//     // End
//
//     function serialize(obj) {
//         let str = [];
//         for (let p in obj) str.push(encodeURIComponent(p) + "=" + obj[p]);
//         return str.join("&");
//     }
//
//     // Filter Product According to the price
//     $("#maxPrice").on('blur', function () {
//         var _min = $(this).attr('min');
//         var _max = $(this).attr('max');
//         var _value = $(this).val();
//         console.log(_value, _min, _max);
//         if (_value < parseInt(_min) || _value > parseInt(_max)) {
//             alert('Values should be ' + _min + '-' + _max);
//             $(this).val(_min);
//             $(this).focus();
//             $("#rangeInput").val(_min);
//             return false;
//         }
//     });
//
//     $("#priceFilterBtn").on('click', function () {
//         var _minPrice = $(this).data('min');
//         var _maxPrice = $('#maxPrice').val();
//         var _filterObj = {};
//         $(".filter-checkbox").each(function (index, ele) {
//             var _filterVal = $(this).val();
//             var _filterKey = $(this).data('filter');
//             _filterObj[_filterKey] = Array.from(document.querySelectorAll('input[data-filter=' + _filterKey + ']:checked')).map(function (el) {
//                 return el.value;
//             });
//         });
//         _filterObj.minPrice = _minPrice;
//         _filterObj.maxPrice = _maxPrice;
//         // Run Ajax
//         $.ajax({
//             url: '/filter-data',
//             data: _filterObj,
//             dataType: 'json',
//             beforeSend: function () {
//                 $(".ajaxLoader").show();
//             },
//             success: function (res) {
//                 console.log(res);
//                 $("#filteredProducts").html(res.data);
//                 $(".ajaxLoader").hide();
//             }
//         });
//     });
//     // End
// });


const postBox =document.getElementById('posts-box');

const loadBtn =document.getElementById('load-btn');
const loadBox =document.getElementById('loading-box');


let visible =3;



const handleGetData =() =>{
      $.ajax({
            type: 'GET',
            url: `/loading/${visible}/`,
            success: function(response){
                // console.log(response.max)
                max_size =response.max;
                console.log(max_size)
                const news =response.news;


                setTimeout(() =>{

                     news.map(news=>{
                    console.log(news.id);
                    postBox.innerHTML+=
             `<div class="news__body body-crd"><a href="{% url 'article' news.slug %}" class="news__card card-tmp">
                <div class="news__lbox card-tmp__lbox">
                    <div class="news__img-box card-tmp__img-ns-box">
                        <img src="${ news.image.url }" alt="#" class="news__img card-tmp__img-ns">
                    </div>
                </div>
                <div class="news__rbox card-tmp__rbox">
                        <div class="news__title-m card-tmp__title ">${news.name }</div>
                    <p class="news__txt card-tmp__txt">
                        ${news.description }
                    </p>
             
                    <ul class="news__list card-tmp__list card-tmp__list_clock">
                        <li class="news__item card-tmp__item card-tmp__item">{% trans 'Время чтения:' %} <span class="txt-bold">${ news.time } {% trans 'минут' %}</span></li>
                    </ul>
                </div>
            </a></div>`
                                                    })
                     if(max_size){

                    loadBox.innerHTML="<center><h4>no news</h4></center>"
                }
                },500)

            },
            error:function(error) {
                console.log(error);

            },
        });
}
handleGetData()


// var el = document.getElementById('overlayBtn');
// if(el){
//   el.addEventListener('click', swapper, false);
// }


loadBtn.addEventListener('click',()=>{
    visible +=3
    handleGetData()
})