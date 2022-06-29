
import random
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

map = [rock, paper, scissors]

yours = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper, 2 form Scissors."))
print(map[yours])

computer = random.randint(0, 2)
print(map[computer])
# 바위(0) 바위(0) -> 무승부
# 0 보(1) -> You Lose -1
# 0 가위(2) -> 이김

# 보(1) 바위(0) -> 이김
# 보 보2 -> 무승부
# 보(1) 가위(2) -> 짐 -1

# 가위 바위 -> 짐
# 가위 보 -> 이김
# 가위 가위 -> 무승부

# draw -> a minus b = 0
# you lose -> com > yours
# you win -> com < yours
# 나 바위 컴 가위 -> 이김
# 나 가위 컴 바위 -> 짐

# 무승부 항상 0

if yours == 0 and computer == 2:
    print("You win")
elif yours == 2 and computer == 0:
    print("You lose")
elif yours < computer:
    print("You Lose")
elif yours > computer:
    print("You win")
elif computer == yours:
    print("Draw")
