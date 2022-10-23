// Code snippet from jQuery Timepicker to show custom times to the form field
$(document).ready(function () {
    $('#id_time_for_visit').timepicker({
        timeFormat: 'HH:mm',
        interval: 30,
        minTime: '8',
        maxTime: '16:00',
        defaultTime: '13',
        startTime: '8:00',
        dynamic: false,
        dropdown: true,
        scrollbar: true
    });
});

// Making the alerts dissapear after 3 seconds
setTimeout(fade_out, 3000);

function fade_out() {
    $('.alert').fadeOut().empty();
}