$( document ).ready(function() {
    
    $("#search").click(function(e) {
        send_ajax($("#in_text").val())
        e.preventDefault()
    });

    function send_ajax(){
        data={
            'csrfmiddlewaretoken':CSRF_TOKEN,
            'username' : $("#username").val(),
            };
        console.log(data);
        // alert("add")
        console.log("data");

        $.ajax({
            type: 'POST',
            url: URL,
            dataType: 'json',
            data:data,
            success: function(res) {
                console.log(res);
                show_items(res)
            }
        });
    }

    function show_items(data){
        my_ul_tag = $('#searched')
        my_ul_tag.empty()
        for (obj in data) {
            o = data[obj]
            var div1 = document.createElement("div");
            div1.className = "col-sm-4";
            var div2 = document.createElement("div");
            div2.className = "panel panel-danger";
            var div3 = document.createElement("div");
            div3.className = "panel-heading";
            var div4 = document.createElement("div");
            div4.className = "panel-body";
            var div5 = document.createElement("div");
            div5.className = "panel-footer";
            ////////////
            var createA = document.createElement('a');
            var createAText = document.createTextNode('cancle');
            createA.style.color = "red";
            createA.setAttribute('href', `cancle_reserve_manager/${o['pk']}`);
            createA.appendChild(createAText);
            div3.append(createA);
            //////////
            var createA3 = document.createElement('p');
            var createAText2 = document.createTextNode(`room: ${o['room']}, price: ${o['price']}`);
            createA3.appendChild(createAText2);
            createA3.style.color = "black";
            div4.append(createA3);
            /////////
            var createA3 = document.createElement('p');
            var createAText2 = document.createTextNode(`stayimg times: ${o['staying_time']}`);
            createA3.appendChild(createAText2);
            createA3.style.color = "black";
            div5.append(createA3);
            div1.append(div2);
            div2.append(div3);
            div2.append(div4);
            div2.append(div5);
            my_ul_tag.append(div1);
        }     
    }
});