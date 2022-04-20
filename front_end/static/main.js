(function($) {
    $('form').submit(function(event){
        event.preventDefault();
        
        var data = new FormData(this);

        var action = function(data) {
            console.log(data)
        }

        $.ajax({
            url: '/api/upload/',
            data:data,
            type: "POST",
            contentType: false,
            processData: false,
            success: action,
            error: action,
        })
    })
})