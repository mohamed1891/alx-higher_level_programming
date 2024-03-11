#!/usr/bin/node
// A script that prints a square

const args = process.argv.slice(2);
const size = parseInt(args[0]);

if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
