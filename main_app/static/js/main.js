$('button').on('click', function(event){
    event.preventDefault();
    var element = $(this);
    $.ajax({
        url : '/clap_auto/',
        type : 'GET',
        data : { auto_id : element.attr("data-id")},

        success : function(response){
            element.html(' ' + response);
        }
    });  
});