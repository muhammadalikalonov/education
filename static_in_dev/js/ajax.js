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

                });
            });

        });

        

    });

function searchSuccess(data, textStatus, jqXHR) {
    // console.log(data)
    $('#filteredUni').html(data.data);
}