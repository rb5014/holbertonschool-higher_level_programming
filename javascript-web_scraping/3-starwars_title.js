#!/usr/bin/node
const request = require('request');
const myUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(myUrl, function (error, response, body) {
  if (error) { console.error('error:', error); } // Print the error if one occurred
  console.log(JSON.parse(body).title); // Print the HTML for the Google homepage.
});
