#!/usr/bin/node
const fs = require('fs');
const data = process.argv[3];
fs.writeFile(process.argv[2], data, (error) => {
  if (error) { console.log(error); }
});
