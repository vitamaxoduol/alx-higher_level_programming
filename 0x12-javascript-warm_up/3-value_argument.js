#!/usr/bin/node

const counts = process.argv;

if (typeof counts[2] === 'undefined') {
  console.log('No argument');
} else {
  console.log(counts[2]);
}
