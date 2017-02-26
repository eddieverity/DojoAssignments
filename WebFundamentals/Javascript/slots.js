function slots(tries) {
  for (var i = tries;i>0;i--) {
    var one_to_onehundred = ((Math.floor(Math.random()*100+1)));
   //   console.log(one_to_onehundred);
    if (one_to_onehundred === 100) {
      var winnings = ((Math.floor(Math.random()*50+51)));
      var i = i+winnings
      console.log("You win " + winnings + " quarters, this brings your total to " + i);
    }
  }
console.log("You ran out of quarters, better luck next time!")
}
slots(100);