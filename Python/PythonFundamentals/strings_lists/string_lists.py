statement = "If monkeys like bananas, then I must be a monkey!"
print statement.find("monkey")
new_statement = statement.replace("monkey","alligator")
print new_statement
arr = [1,54,-2,7,12,98]
#print min & max of an array
print min(arr)
print max(arr)
#print first & last positions of an array
print arr[0]
print arr[-1]
#print new array with first and last positions
new_arr = [arr[0],arr[-1]]
print new_arr
#print sorted x
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
#take a list, sort it, split it in half then add it as a list within that original list
y = x[:(len(x)/2)]
x = x[(len(x)/2):]
x.insert(0,y)
print x


