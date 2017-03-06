def s_g():
  import random
  random_num = random.random()*40+61
  if random_num >= 90:
    print "Score: " + str(random_num) + "; Your grade is A"
  elif random_num >= 80:
    print "Score: " + str(random_num) + "; Your grade is B"
  elif random_num >= 70:
    print "Score: " + str(random_num) + "; Your grade is C"
  else:
    print "Score: " + str(random_num) + "; Your grade is D"

s_g()