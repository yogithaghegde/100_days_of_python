rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
#computer should generate random value
import random
comp = random.randint(0,2)
player = int(input("What do you choose? type 0 for Rock,1 for Paper,2 for Scissors"))
image = [rock,paper,scissors]

print('Computer')
print(image[comp])


print("Player")
if player <2:
  print(image[player])
else:
  print('invalid')



  
if comp ==0 and player ==1:
  print("you win")
elif comp ==0 and player ==2:
  print("you lose")
elif comp ==1 and player ==0:
  print("you lose")
elif comp ==1 and player ==2:
  print("you win")
elif comp ==2 and player ==0:
  print("you win")
elif comp ==2 and player ==1:
  print("you lose")
elif comp == player:
  print('Tie')
