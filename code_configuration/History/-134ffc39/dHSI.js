/*
  Write a function `isAnagram` which takes 2 parameters and returns true/false if those are anagrams or not.
  What's Anagram?
  - A word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp.
*/

function isAnagram(str1, str2) {
  a = str1.split("").sort().join("").toLowerCase();
  b = str2.split("").sort().join("").toLowerCase();
  console.log(a, b);
  if(a == b){
    return true;
  }
  else{
    return false;
  }
}

module.exports = isAnagram;