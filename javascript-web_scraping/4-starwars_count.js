#!/usr/bin/node
const request = require('request');
const myUrl = process.argv[2];
request(myUrl, function (error, response, body) {
  if (error) { console.error('error:', error); } // Print the error if one occurred
  const films = JSON.parse(body);
  const count = films.results.filter(film => film.characters.filter(char => char.includes('18')).length > 0).length;
  console.log(count);
});
