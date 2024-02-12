$(document).ready(function () {
    $('INPUT#btn_translate').click(function () {
        $.ajax({
            type: 'GET',
            url: 'https://www.fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val(),
            success: function (data) {
                $('DIV#hello').text(data.lang);
            }
        });
    });
});
