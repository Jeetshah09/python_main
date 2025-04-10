def rockpaper():
  p1=input("p1 turn choose(rock,scissors,paper): ")
  p2=input("p2 turn choose(rock,scissors,paper): ")
  print("p1 choose:",p1)
  print("p2 choose:",p2)
  if p1==p2:
    print("match is tie")
  elif(p1=='rock' and p2=="scissors"):
    print("p1 is win")
  elif(p1=='scissors' and p2=="paper"):
    print("p1 is win")
  elif(p1=='paper' and p2=="rock"):
    print("p1 is win")
  else:
    print("p2 is win")

def game():
  ch =input("enter your input\ns for new game:")
  if ch=='s':
    rockpaper()
    game()
  else:
    print("thank you")

game()
