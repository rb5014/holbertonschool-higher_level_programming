#!/usr/bin/node
function getSecondBiggest (arr) {
  let biggest = 0;
  let secondBiggest = 0;
  for (let i = 0; i < arr.length; i++) {
    const num = parseInt(arr[i]);
    if (num > biggest) {
      secondBiggest = biggest;
      biggest = num;
    } else if (num > secondBiggest) {
      secondBiggest = num;
    }
  }
  return secondBiggest;
}

if (process.argv.length <= 3) {
  console.log(0);
} else {
  console.log(getSecondBiggest(process.argv));
}
