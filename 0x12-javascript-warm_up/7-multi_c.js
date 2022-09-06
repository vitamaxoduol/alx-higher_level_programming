#!/usr/bin/node

const x = process.argv[2];

if (typeof x === 'undefined') {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= x; i++) {
    console.log('C is fun');
  }
}
