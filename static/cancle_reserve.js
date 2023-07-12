$( document ).ready(function() {
    $("button").click(function(e) {
        item_id = e.target.id;
        send_ajax()

    });

    function send_ajax(){
        
        data={
            'csrfmiddlewaretoken':CSRF_TOKEN,
            'item':item_id,
            };
        console.log(data);

        $.ajax({
            type: 'POST',
            url: URL,
            dataType: 'json',
            data:data,
            
            success: function(res) {
                console.log(res);
                alert("deleted");
            },
            always: function() {
                console.log(data);
                alert("deleted")
            }
        });
    };
});