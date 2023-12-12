#!/usr/bin/node

const arg = process.argv.length;

if (arg <= 3) {
  console.log(0);
} else {
  const args = [];
  for (let i = 2; i < arg; i++) {
    args.push(process.argv[i]);
  }
  args.sort();
  console.log(args[args.length - 2]);
}
