$(document).ready(function() {
    var frm = $('#ans-form');
    frm.submit(function () {
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            success: function (data) {
                if (data['isCorrect'] == 'false') {
                    // if answer is wrong, 
                    // stay on the page and display message.
                    $("#response").html(data['responseText']);
                }
                else {
                    // redirect to the next question page
                    // if the answer is correct
                    window.location.href = "/sherlocked/play";
                }
            },
            error: function(data) {
                $("#response").html("Something went wrong!");
            }
        });
        return false;
    });
});