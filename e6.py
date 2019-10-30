#print("Testing on Terminal")
#name= input("What is your name?\n")
#print("Hello,",name)
#== lab5 ex10==
class Computer:
   def __init__(self,cpu,color,portability):
      self.c =cpu
      self.co =color
      self.p =portability

   def playgame(self, nameofgame):
      if self.p:
          print("you are playing",nameofgame,"on your laptop!")
      else:
          print("you are playing",nameofgame,"on your desktop.")

class laptop(Computer):
   def __init__(self,cpu,color):
      Computer.__init__(self,cpu,color,'True')
class desktop(Computer):
   def __init(self,cpu,colour):
     Computer.__init__(self,cpu,colour,'False')
myMac = laptop("A6","White")
print("My PC runs on",myMac.c)
myMac.playgame("Dooms Day")
