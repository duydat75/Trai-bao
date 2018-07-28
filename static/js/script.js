$(document).ready( function() {
    $("#newlover").on("click", function() {
        // $("#bot-step-2-1").load("lover");
        $("#bot-step-2-1").load("newlover");
        $("#bot-step-2 .avatar").show();
        document.getElementById('lover').disabled = true;
    });
    $("#lover").on("click", function() {
        $("#bot-step-2-2").load("lover");
        $("#bot-step-2 .avatar").show();
        document.getElementById('newlover').disabled = true;
    });
    $("#di-dau").on("click", function() {
        $("#bot-step-4").show();
        $("#user-step-3").show();
        // $(".chatbot").append(
        //     '<div id="user-step-2" class="user">' +
        //     '<span class="user-mess bg-transparent"><input type="button" id="di-dau" value="Đi đâu" /></span>'+
        //     '<span class="user-mess bg-transparent"><input type="button" id="mua-gi" value="Mua gì"></span>'+
        //     '<img src="../static/image/male-profile.jpg" alt="" class="avatar ml-2">'+
        //     '</div>'
        // );
    });
    $("#nha-hang").on("click", function() {
        $("#bot-step-5").load("nhahang");
    })

    $("#nha-nghi").on("click", function() {
        $("#bot-step-5").load("nhanghi");
    })

    $("#sieu-thi").on("click", function() {
        $("#bot-step-5").load("sieuthi");
    })
    
    // $("#new").on("click", function() {
    //     $("#bot-step-2-3").load("newlover");
    // });
    // $('.b1').click(function(){
    //     $('div').append('<input type="text"..etc ');
    // });  
    
});