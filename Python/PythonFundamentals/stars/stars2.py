x = [4,"Tom",1,"Michael",5,7,"Jimmy Smith"]
def draw_stars(a):
  for i in x:
    if type(i) is int:
      print "*"*i
    else:
      print (i[0]*len(i)).lower()
draw_stars(x)