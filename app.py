import sys
from time import sleep
from modules import athleticfit, bodyrecomp, buildmuscle, losefat

# Typing Text Generator
speed = 0.02  # Seconds between new character
def typeP(words):
    for char in words:
        sleep(speed)
        sys.stdout.write(char)
        sys.stdout.flush()

header = '''
███████╗██╗████████╗███████╗██████╗ ███████╗ █████╗ ██╗  ██╗
██╔════╝██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔══██╗██║ ██╔╝
█████╗  ██║   ██║   █████╗  ██████╔╝█████╗  ███████║█████╔╝
██╔══╝  ██║   ██║   ██╔══╝  ██╔══██╗██╔══╝  ██╔══██║██╔═██╗
██║     ██║   ██║   ██║     ██║  ██║███████╗██║  ██║██║  ██╗
╚═╝     ╚═╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
'''

print(header)
typeP("Welcome to FitFreak!\nTrain Smart, Get Fit, Live Strong!!!\n")
name = input("Enter your name:")
typeP("Hello " + name + "!\nGet fit with our next-gen fitness app.\nPersonalized workouts, easy navigation, "
                    "and progress tracking.\nStart your fitness journey today!\n")
typeP("What is your fitness level?\n1. Beginner\n2. Intermediate\n3. Expert\n")

while True:
    level = input("TYPE IN YOUR RESPONSE:\n").lower()
    if(level == "beginner") or (level == "intermediate") or (level == "expert"):
        break
    print("Invalid Input! Please try again!!!")

typeP("Choose your fitness goal:\n1. Build Muscle\n2. Lose Fat\n3. Body Recomposition\n4. Athletic "
      "Fitness\n")
while True:
    goal = input("SELECT THE APPROPRIATE OPTION:\n")

    if goal == '1':
        typeP("Your personalized workout plan is here:\n")
        buildmuscle.buildMuscle(level)
        break
    elif goal == '2':
        typeP("Your personalized workout plan is here:\n")
        losefat.loseFat(level)
        break
    elif goal == '3':
        typeP("Your personalized workout plan is here:\n")
        bodyrecomp.bodyrecomp(level)
        break
    elif goal == '4':
        typeP("Your personalized workout plan is here:\n")
        athleticfit.athleticFit(level)
        break
    else:
        print("Invalid input! Please try again!!!")

