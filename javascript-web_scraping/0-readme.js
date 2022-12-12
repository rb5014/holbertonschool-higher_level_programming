#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], function (error, data) {
  if (error) {
    console.log(error);
  } else {
    console.log(data.toString());
  }
});
