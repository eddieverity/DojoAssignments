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
 Create a program that outputs:

Michael Jordan
John Rosales
Mark Guillen
KB Tonel

*/

function outputStudents() {
  for (var i = 0;i<users.Students.length;i++) {
    console.log(users.Students[i].first_name + " " + users.Students[i].last_name);
  }
}
outputStudents();