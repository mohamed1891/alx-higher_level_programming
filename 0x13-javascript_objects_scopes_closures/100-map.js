#!/usr/bin/node

// Import the initial list from 100-data.js
const list = require('./100-data').list;

// Compute a new list where each value is multiplied by its index
const newList = list.map((value, index) => value * index);

// Print the initial list
console.log('Initial list:');
console.log(list);

// Print the new list
console.log('New list (values multiplied by index):');
console.log(newList);
