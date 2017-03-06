users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
}

def roster(dict):
  for key, data in users.items():
    print key
    i = 0
    for value in data:
      i+=1
      print i, "-", value["first_name"].upper(), value["last_name"].upper(), "-", len(value["first_name"]) + len(value["last_name"])
roster(users)