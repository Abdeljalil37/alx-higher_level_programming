#!/usr/bin/node

const fs = require('fs');

const outputFile = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(outputFile, stringToWrite, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
