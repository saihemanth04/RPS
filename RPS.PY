import random

comp = random.choice([1,2,3])
print("Welcome to Rock, Paper, Scissors!")
yourcho=input(str("Choose rock, paper, or scissors: "))
youdict={
  "rock":1,
  "paper":2,
  "scissors":3
}
compdict={
  1:"rock",
  2:"paper",
  3:"scissors"
}
you=youdict[yourcho]
compc=compdict[comp]
print(f"the computer chose {compc}")
if(you==comp):
   print("Draw match")
elif(you==1 and comp==2):
  print("Computer wins")
elif(comp==1 and you==2):
  print("you win")
elif(you==1 and comp==3):
  print("you win")
elif(comp==1 and you==3):
  print("computer wins")
elif(you==2 and comp==3):
  print("computer wins")
elif(comp==2 and you==3):
  print("you win")
else:
  print("error")