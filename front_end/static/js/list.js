$(document).ready(function(){
    $.ajax({
        type: 'get',
        url: '/api/list/',
        dataType: 'json',
        success: function (data) {
            Object.keys(data).forEach(key =>{
                for (let transactions of data[key].transactions.entries()){
                    $('#body').append(
                        "<tr>",
                        "<td>" + key + "</td>",
                        "<td>" + data[key].total + "</td>",
                        "<td>" + transactions[1].type + "</td>",
                        "<td>" + transactions[1].value + "</td>",
                        "<td>" + transactions[1].cpf + "</td>",
                        "<td>" + transactions[1].card + "</td>",
                        "<td>" + transactions[1].date + "</td>",
                        "<td>" + transactions[1].hour + "</td>",
                        "</tr>",
                    );
                }
            })
        },
        error: function (xhr, status, error) {
            console.log(xhr, error);
        }
    })
});
