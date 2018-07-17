$(document).ready( function() {
    $('#next').click(function() {
       $.ajax("{{ url_for('lover') }}").done(function (reply) {
          $('#container').html(reply);
       });
    });
});