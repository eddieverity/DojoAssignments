function ragsToRiches (total) {
  var penny = .01;
  var running_total = 0;
  var days = 0;
  for (var i = 0;i<=total;i=running_total) {
    running_total=running_total+penny;
    penny=penny*2;
    days++;
  }
  console.log("It took the servant " + days + " days to make $" + total);
}


ragsToRiches(10000);