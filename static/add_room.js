$( document ).ready(function() {
    $("#submit").click("input", function() {
        console.log("xxxxxxxxxxx")
        send_ajax()
    });

    function send_ajax(){
        data={
            'csrfmiddlewaretoken':CSRF_TOKEN,
            'room_number' : $("#number").val(),
            'capacity' : $("#capacity").val(),
            'price': $("#price").val(),
            };
        console.log(data);
        alert("add")
        console.log("data");

        $.ajax({
            type: 'POST',
            url: URL,
            dataType: 'json',
            data:data,
            
            success: function(res) {
                console.log(res);
            },
            always: function() {
                console.log(data);
            }
        });
    }
});