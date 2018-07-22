$(document).ready( function() {
    console.log("buzzz");
    
    $('#next').click(function() {
       $.ajax("{{ url_for('newlover') }}").done(function (reply) {
          $('#container').html(reply);
       });
    });
});

// $(document).ready( function() {
//     $('#next1').click(function() {
//        $.ajax("{{ url_for('lover') }}").done(function (reply) {
//           $('#container').html(reply);
//        });
//     });
// });
