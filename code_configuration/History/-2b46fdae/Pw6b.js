/*
  Implement a function `calculateTotalSpentByCategory` which takes a list of transactions as parameter
  and return a list of objects where each object is unique category-wise and has total price spent as its value.
  Transaction - an object like { itemName, category, price, timestamp }.
  Output - [{ category1 - total_amount_spent_on_category1 }, { category2 - total_amount_spent_on_category2 }]
*/

function calculateTotalSpentByCategory(transactions) {
  arr = {};
  for(let i = 0; i < transactions.length; i++){
    let cat = transactions[i].category;
    console.log(cat);
    if(cat in arr)
      arr.cat = arr.cat + price; 
    else 
      arr.cat = 0;
  }
  return arr;
}

module.exports = calculateTotalSpentByCategory;
