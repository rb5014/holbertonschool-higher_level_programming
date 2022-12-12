#!/usr/bin/node
const request = require('request');
const myUrl = 'https://swapi-api.hbtn.io/api/films/';
request(myUrl, function (error, response, body) {
  if (error) { console.error('error:', error); } // Print the error if one occurred
  const films = JSON.parse(body);
  let count = 0;
  for (let i = 0; i < films.results.length; i++) {
    if (films.results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      count += 1;
    }
  }
  console.log(count);
});
