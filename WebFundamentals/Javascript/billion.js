function ragsToRiches (days) {
  var penny = .01;
  var total = 0;
  for (var i = 1; i <= days;i++) {
    total = total + penny;
    penny = penny*2;
  }
  console.log("The servant made $" + total);
}
ragsToRiches(30)