#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const myUrl = process.argv[2];
const filePath = process.argv[3];
request(myUrl, function (error, response, body) {
  if (error) { console.error('error:', error); } // Print the error if one occurred
  const data = body;
  fs.writeFile(filePath, data, (error) => {
    if (error) { console.log(error); }
  });
});
