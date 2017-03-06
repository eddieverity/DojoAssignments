def coin_toss():
  import random
  counter_heads = 0
  counter_tails = 0
  flips = 0
  for i in range(1,101):
    flips += 1
    x = random.random()
    x = round(x)
    if x == 1:
      counter_heads+=1
      print "Attempt #" + str(flips) + ": Throwing a coin... It's a head! ... got " + str(counter_heads) + " heads and " + str(counter_tails) + " tails so far"
    else:
      counter_tails+=1
      print "Attempt #" + str(flips) + ": Throwing a coin... It's a head! ... got " + str(counter_heads) + " heads and " + str(counter_tails) + " tails so far"
  print "Ending program, thank you!"
coin_toss()
