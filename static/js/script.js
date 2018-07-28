$(document).ready( function() {
    $("#new").on("click", function() {
        // $("#bot-step-2-1").load("lover");
        $("#bot-step-2-1").load("newlover");
        $("#bot-step-2 .avatar").show();
        document.getElementById('lover').disabled = true;
    });
    $("#lover").on("click", function() {
        $("#bot-step-2-2").load("lover");
        $("#bot-step-2 .avatar").show();
        document.getElementById('next').disabled = true;
    });
    
    // $("#new").on("click", function() {
    //     $("#bot-step-2-3").load("newlover");
    // });
    // $('.b1').click(function(){
    //     $('div').append('<input type="text"..etc ');
    // });  
    
});