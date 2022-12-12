#!/usr/bin/node
const request = require('request');
const myUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(myUrl, function (error, response, body) {
  if (error) { console.error('error:', error); } // Print the error if one occurred
  const filmDict = JSON.parse(body);
  for (const ch of JSON.parse(body).characters) {
    request(ch, function (err, response, body) {
      if (err) {
        console.log(err);
      } else {
        console.log(JSON.parse(body).name);
      }
    });
  }
});
