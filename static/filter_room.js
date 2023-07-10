$( document ).ready(function() {
    $("#submit").click("input", function() {
        console.log("xxxxxxxxxxx")
        send_ajax()
    });

    function send_ajax(){
        data={
            'csrfmiddlewaretoken':CSRF_TOKEN,
            'filter' :$("#filter :selected").text(),
            };
        console.log(data);
        alert("ok")
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