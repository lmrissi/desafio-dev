(function($) {
    $('form').submit(function(event){
        event.preventDefault();
        
        var data = new FormData(this);
        data += "Content-Disposition: form-data; name=\"query\"; \r\n";

        var action = function(data) {
            console.log(data)
            console.log(myUrl)
        }

        var filename = $('input[type=file]').val().split('\\').pop();
        var myUrl = '/api/upload/'

        console.log(myUrl)

        $.ajax({
            url: myUrl,
            body: data,
            type: "POST",
            contentType: false,
            contentDispostion: "CNAB.txt",
            processData: false,
            success: action,
            error: action,
        })
    })
})