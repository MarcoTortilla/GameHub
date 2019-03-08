print("Hello, and welcome to HollyWood's Fortnite Trivia Game")
print("***Type the letter (lowercase) in which you think is the answer***")
print("Your results will be displayed at the end out of 54")
def questions():
  points = 0
  print("-----------------------------------------------------")
  print("1.) When did Fortnite Battle Royale release?")
  a = ("A.) 1-23-2017")
  b = ("B.) 6-18-2018")
  c = ("C.) 9-27-2016")
  d = ("D.) 7-25-2017")
  print(a)
  print(b)
  print(c)
  print(d)
  answer = input()
  if answer == ("d"):
    points = points + 1
  elif answer == ("a"):
    points = points
  elif answer == ("b"):
    points = points
  elif answer == ("c"):
    points = points
  print("2.) Who was the most mainstream streamer for Fortnite?")
  print("A.) Ninja")
  print("B.) TSM_Daequan")
  print("C.) Tfue")
  print("D.) Drake")
  a = ("A.) Ninja")
  b = ("B.) TSM_Daequan")
  c = ("C.) Tfue")
  d = ("D.) Drake")
  answer2 = input()
  if answer2 == ("a"):
    points = points + 2
  elif answer2 == ("b"):
    points = points
  elif answer2 == ("c"):
    points = points
  elif answer2 == ("d"):
    points = points
  print("3.) In what season did Fortnite include rifts?")
  print("A.) Season 1")
  print("B.) Season 4")
  print("C.) Season 5")
  print("D.) Season 8")
  a = ("A.) Season 1")
  b = ("B.) Season 4")
  c = ("C.) Season 5")
  d = ("D.) Season 8")
  answer3 = input()
  if answer3 == ("c"):
    points = points + 3
  elif answer3 == ("a"):
    points = points
  elif answer3 == ("b"):
    points = points
  elif answer3 == ("d"):
    points = points
  print("4.) What streamer says 'I Hit Those'?")
  print("A.) Ninja")
  print("B.) TSM_Daequan")
  print("C.) Tfue")
  print("D.) TSM_Myth")
  a = ("A.) Ninja")
  b = ("B.) TSM_Daequan")
  c = ("C.) Tfue")
  d = ("D.) TSM_Myth")
  answer4 = input()
  if answer4 == ("b"):
    points = points + 4
  elif answer4 == ("a"):
    points = points
  elif answer4 == ("b"):
    points = points
  elif answer4 == ("d"):
    points = points
  print("5.) What was the first vehicle in Fortnite?")
  print("A.) Rifts")
  print("B.) Golf Kart")
  print("C.) Shopping Cart")
  print("D.) Quadcrasher")
  a = ("A.) Rifts")
  b = ("B.) Golf Kart")
  c = ("C.) Shopping Cart")
  d = ("D.) Quadcrasher")
  answer5 = input()
  if answer5 == ("c"):
    points = points + 5
  elif answer5 == ("a"):
    points = points
  elif answer5 == ("b"):
    points = points
  elif answer5 == ("d"):
    points = points
  print("6.) How do players enter the Fortnite map?")
  print("A.) Swim")
  print("B.) Battle Boat")
  print("C.) Battle Bus")
  print("D.) Battle Plane")
  a = ("A.) Swim")
  b = ("B.) Boat")
  c = ("C.) Bus")
  d = ("D.) Plane")
  answer6 = input()
  if answer6 == ("c"):
    points = points + 6
  elif answer6 == ("a"):
    points = points
  elif answer6 == ("b"):
    points = points
  elif answer6 == ("d"):
    points = points
  print("7.) What is the most famous POI (point of interest)?")
  print("A.) Tilted Towers")
  print("B.) Dusty Divot")
  print("C.) Loot Lake")
  print("D.) Pleasant Park")
  a = ("A.) Tilted Towers")
  b = ("B.) Dusty Divot")
  c = ("C.) Loot Lake")
  d = ("D.) Pleasant Park")
  answer7 = input()
  if answer7 == ("a"):
    points = points + 7
  elif answer7 == ("b"):
    points = points
  elif answer7 == ("c"):
    points = points
  elif answer7 == ("d"):
    points = points
  print("8.) What artist had their own concert event in-game?")
  print("A.) Drake")
  print("B.) Marshmello")
  print("C.) Lil Yachty")
  print("D.) XXXTENTACION")
  a = ("A.) Drake")
  b = ("B.) Marshmello")
  c = ("C.) Lil Yachty")
  d = ("D.) XXXTENTACION")
  answer8 = input()
  if answer8 == ("b"):
    points = points + 8
  elif answer8 == ("a"):
    points = points
  elif answer8 == ("c"):
    points = points
  elif answer8 == ("d"):
    points = points
  print("9.) What was the first event ever held in fortnite?")
  print("A.) Cube event")
  print("B.) Earthquake event")
  print("C.) Fortnitemares event")
  print("D.) Rocket Launch event")
  a = ("A.) Cube event")
  b = ("B.) Earthquake event")
  c = ("C.) Fortnitemares event")
  d = ("D.) Rocket Launch event")
  answer9 = input()
  if answer9 == ("d"):
    points = points + 8
  elif answer9 == ("a"):
    points = points
  elif answer9 == ("c"):
    points = points
  elif answer9 == ("b"):
    points = points
  print("10.) What area was destroyed in the beginning of season 4?")
  print("A.) Tilted Towers")
  print("B.) Anarchy Acres")
  print("C.) Dusty Divot")
  print("D.) Dusty Depot")
  a = ("A.) Tilted Towers")
  b = ("B.) Anarchy Acres")
  c = ("C.) Dusty Divot")
  d = ("D.) Dusty Depot")
  answer10 = input()
  if answer10 == ("d"):
    points = points + 10
  elif answer10 == ("a"):
    points = points
  elif answer10 == ("c"):
    points = points
  elif answer10 == ("b"):
    points = points

  print("Your Total Score is:")
  print(points)
  if points == (54):
    print("Great Job You got a PERFECT SCORE!!!!!")
questions()


import hub
