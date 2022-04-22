(function($) {
    $('form').submit(function(event){
        event.preventDefault();
        
        var data = new FormData(this);

        $.ajax({
            url: '/api/upload/',
            body: data,
            type: "POST",
            contentType: false,
            processData: false,
        })
    })
})