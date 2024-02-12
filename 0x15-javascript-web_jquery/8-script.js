$(document).ready(function () {
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        type: 'GET', success: function(data){
            for (let i =0 ; i < data.results.length; i++){
                $('UL#list_movies').append('<li>' + data.results[i].title + '</li>')
            }
        }
    });
});
