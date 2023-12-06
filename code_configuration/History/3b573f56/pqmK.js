/*
  Implement a function `isPalindrome` which takes a string as argument and returns true/false as its result.
  Note: the input string is case-insensitive which means 'Nan' is a palindrom as 'N' and 'n' are considered case-insensitive.
*/

function isPalindrome(str) {
  var i, j;
  for(i=0, j = str.length-1; i<j; i++, j--)
  return true;
}

module.exports = isPalindrome;
