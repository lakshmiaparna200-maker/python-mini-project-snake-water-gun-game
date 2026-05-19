import random
#0 for  gun
#for water
 #  for snake '''
computer=random.choice([0,-1,1])
you=input("enter your choice:")
youDict={"s":-1,"w":1,"g":0}
reverseDict={-1:"snake",1:"water",0:"gun"}
you= youDict[you]
# by now there are two numbers(variables),you and computer
print(f"you choose{reverseDict[you]}\n computer choose {reverseDict[computer]}")

if(computer==you):
 print("it's a draw")
else:
     if(computer==-1 and you == 1):
        print("you loose !")
     elif(computer==0 and you == 1):
          print("you loose!")
     elif(computer==1 and you == -1):
          print("you loose!")
     elif(computer==0 and you ==-1):
          print("you loose!")
     elif(computer==-1 and you == 0):
          print("you loose!")
     elif(computer==1 and you == 0):
         print("you loose!")
     else:
       print("something went wrong")
   
        