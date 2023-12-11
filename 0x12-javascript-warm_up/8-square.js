#!/usr/bin/node

let x = '';
if (parseInt(process.argv[2])) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      x += 'X';
    }
    console.log(x);
    x = '';
  }
} else {
  console.log('Missing size');
}
