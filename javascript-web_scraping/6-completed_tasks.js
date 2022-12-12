#!/usr/bin/node
const request = require('request');
const myUrl = process.argv[2];
request(myUrl, function (error, response, body) {
  if (error) { console.error('error:', error); } // Print the error if one occurred
  const todos = JSON.parse(body);
  const res = {};
  const listCompleted = Object.values(todos).filter(d => d.completed === true);
  listCompleted.forEach(dict => {
    if (!(dict.userId in res)) {
      res[dict.userId] = 1;
    } else {
      res[dict.userId] += 1;
    }
  });
  console.log(res);
});
