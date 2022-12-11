#!/usr/bin/node
function factorial (num) {
  let result = 1;
  for (let i = num; i > 1; i--) {
    result *= i;
  }
  return result;
}

const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}
