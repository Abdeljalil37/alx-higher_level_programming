#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, body) => {
    if (error) {
        console.error(error);
    } else {
        const movie = JSON.parse(body);
        console.log(movie.title);
    }
});
