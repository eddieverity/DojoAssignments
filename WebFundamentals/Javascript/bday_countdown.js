function bdayCountdown(daysUntilMyBirthday) {
  while (daysUntilMyBirthday>0) {
    if (daysUntilMyBirthday>30) {
      console.log(daysUntilMyBirthday + "days until my birthday ... :(");
        daysUntilMyBirthday = daysUntilMyBirthday - 1;
    }
    else if (daysUntilMyBirthday>=5) {
      console.log(daysUntilMyBirthday + "days until my bday!!! :)");
      daysUntilMyBirthday = daysUntilMyBirthday - 1;
    }
    else {
      console.log(daysUntilMyBirthday + "DAYS UNTIL MY BIRTHDAY!!!!!!!");
      daysUntilMyBirthday=daysUntilMyBirthday-1;
    }
  }
  console.log("ITS MY BIRTHDAY")
}
bdayCountdown(50);