#!/usr/bin/node
const request = require('request');
const myUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(myUrl, function (error, response, body) {
  if (error) { console.error('error:', error); } // Print the error if one occurred
  const filmDict = JSON.parse(body);
  filmDict.characters.forEach(charUrl => {
    request(charUrl, function (error, response, body) {
      if (error) { console.error('error:', error); } // Print the error if one occurred
      const name = JSON.parse(body).name;
      console.log(name);
    });
  });
});
