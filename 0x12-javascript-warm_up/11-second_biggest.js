#!/usr/bin/node

const arg = process.argv.length;
let biggest = 0;
let max = 0;

if (arg <= 3) {
  console.log('1');
} else {
  for (let i = 1; i <= arg; i++) {
    if (parseInt(process.argv[i + 1]) > max) {
      biggest = parseInt(process.argv[i + 1]);
    }
    max = biggest;
  }
  console.log(biggest);
}
