$( document ).ready(function() {
    $("#submit").click("input", function() {
        console.log("xxxxxxxxxxx")
        send_ajax()
    });

    function send_ajax(){
        data={
            'csrfmiddlewaretoken':CSRF_TOKEN,
            'username' : $("#username").val(),
            'email' : $("#email").val(),
            'password': $("#password").val(),
            'role' :$("#role :selected").text(),
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