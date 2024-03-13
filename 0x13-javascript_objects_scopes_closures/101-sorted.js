#!/usr/bin/node
const dict = require('./101-data.js').dict;

const myDict = {};

for (const key in dict) {
  const value = dict[key]; 
  if (!myDict[value]) {
	myDict[value] = [];
  }
  myDict[value].push(key);
}

console.log(myDict);
