var users = {
 'Students': [ 
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'Instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 }

 /* 
Create a program that prints  the following format (including the number of characters in each combined name):

Students
1 - MICHAEL JORDAN - 13
2 - JOHN ROSALES - 11
3 - MARK GUILLEN - 11
4 - KB TONEL - 7
Instructors
1 - MICHAEL CHOI - 11
2 - MARTIN PURYEAR - 13

*/

function outputUsers() {
  for (key in users) {
    console.log(key);
    for (var i = 0;i< users[key].length;i++) {
    var total_length = users[key][i].first_name.length + users[key][i].last_name.length;
    console.log(i+1 + " - " + users[key][i].first_name.toUpperCase() + " " + users[key][i].last_name.toUpperCase() + " - " + total_length);  
    }  
  }
}    
outputUsers();