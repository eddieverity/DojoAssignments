var hour = 7;
var min = 49;
var meridian = "AM";  

if ((min<30) && (meridan=="AM")) {
  console.log("It's just after", hour, "in the morning");
}
else if ((min==30) && (meridian=="AM")) {
  console.log("It's half past", hour, "in the morning");
}
else if ((min>30) && (meridian=="AM")) {
  console.log("It's almost", hour+1, "in the morning");
}
else if ((min<30) && (meridian=="PM")) {
  console.log("It's just after", hour, "in the evening");
}
else if ((min==30) && (meridian=="PM")) {
  console.log("It's half past", hour, "in the evening");
}
else if ((min>30) && (meridian=="PM")) {
  console.log("It's almost", hour+1, "in the evening");
}