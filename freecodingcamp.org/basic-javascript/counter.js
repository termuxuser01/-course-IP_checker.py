//countdown
function countdown(n){
  if (n < 1){
    return [];
  }else {
    const arr = countdown(n - 1);
    arr.unshift(n)
    return arr;
  }
}

//countup
function countup(n) {
  if (n < 1) {
    return [];
  } else {
    const countArray = countup(n - 1);
    countArray.push(n);
    return countArray;
  }
}
