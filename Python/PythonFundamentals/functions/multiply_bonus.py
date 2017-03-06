def multiply(arr,mult):
  z = []
  for i in arr:
    z.append(i*mult)
  return z
b = multiply([2,4,5],3)

def layered(mult):
  new_arr=[]
  mini_arr=[]
  for i in mult:
    mini_arr=[]
    for y in range(0,i):
      (mini_arr.append(1))
    new_arr.append(mini_arr)
  print new_arr
x = layered(multiply([2,3,4],2))
print x