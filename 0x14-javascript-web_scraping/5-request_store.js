#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];

request.get(url, (error, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(process.argv[3], body.body, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
}
);
