import random

target =random.randint(0, 1000)
print(".....Choose a number between 0 to 1000.....")
while True:
    
    userInput= input("Input your Guess or Quit the Game(Q): ")
    if(userInput == "Q"):
        break
    userInput = int(userInput)
    if(userInput==target):
        print("Your guess was correct. YEah!!")
        break
    elif(userInput<target):
        print("Your guess was too low...")
    else:
        print("Your input was too high....")
print("!!!!!!!!!Game over!!!!!!!!!")