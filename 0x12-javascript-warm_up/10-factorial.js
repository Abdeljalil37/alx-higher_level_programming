#!/usr/bin/node

// Factorial function
function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

if (!parseInt(process.argv[2])) {
  console.log('1');
} else {
  console.log(factorial(parseInt(process.argv[2])));
}
