name = "Ed"
name = "Ed Verity"
code = "Python"
answer = 42
print "printing changed variable :"
print name
print "printing math operation:"
print 79.0//2
print "printing addition of two strings:"
print name+code
print "printing str + integer:"
print name + str(answer)
print "different format for str + integer:"
print "answer", answer

print "example of string interpolation:"
print "My name is {} and i'm learning {}".format(name, code)
print "example of string interpolation with different syntax"
print "My name is %s and i'm learning %s" % (name, code)
print " "
print ".capitalize() method on a string"
print name.capitalize()
print name.lower()
print name.swapcase()
print name.upper()
print name.find("er")
print name.replace("Ed", "Edward")
breakfast = "egg egg egg Spam egg Spam"
print breakfast.replace("Spam", "Cheese")
print breakfast.replace("egg", "Cheese", 2)
print "Appending 99 to a list"
x = [1,2,3,4,5]
x.append(99)
print x
print "inserting 99 into 2nd position on a list"
x.insert(2,99)
print x
print "removing position 3 from a list"
x.remove(3)
print x
print "pop on a list"
x.pop()
print x
print "popping position 1"
x.pop(1)
print x
print "sorting a list"
x.sort()
print x
print "slicing a list with x[:]"
print x[:]
print "slicing with x[1:]"
print x[1:]
print "slicing with x[:4]"
print x[:4]
print "slicing with x[2:4]"
print x[2:4]
print "printing len() of a list"
print len(x)
print "printing max() of a list"
print max(x)
print "printing min() of a list"
print min(x)
print "printing any() of a list (for bool=true)"
print any(x)
print "printing all() to check if each item = true"
print all(x)
names = ["name1","name2","name3"]
print "\n".join(names)
