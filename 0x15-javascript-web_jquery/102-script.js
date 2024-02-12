$(document).ready(function () {
    $('INPUT#btn_translate').click(function () {
        $.ajax({
            url: 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + $('INPUT#language_code').val(),
            type: 'GET',
            success: function (data) {
                $('DIV#hello').text(data.hello);
            }
        });
    });
});
