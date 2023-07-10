# Athletic Fitness Module of FitFreak
from modules import exercises

# Bold Color ANSI Escape Sequence

# Motivation for muscle building here


# Workout plan for muscle building:
split = ("Cardio + Chest", "Arms + Back", "Lower + Shoulders", "Cardio + Abs", "Lower + Arms")
plan = dict({"Monday": split[0], "Tuesday": split[1], "Wednesday": split[2], "Thursday": split[3], "Friday": split[4],
             "Saturday": split[3], "Sunday": "Rest"})


# Printing workout plan
def printWorkout(workouts):
    for workout in workouts:
        print("Name: " + workout.get("name"))
        print("Workout Type: " + workout.get("type"))
        print("Muscle: " + workout.get("muscle"))
        print("Equipments needed: " + workout.get("equipment"))
        print("Instructions:")
        ins = workout.get("instructions").rstrip().split('.')
        for line in ins:
            if line == " ": continue
            print(line.strip())


# Workouts
def cardioWorkouts(level, day):
    cardio = exercises.getExerciseType("cardio", level)

    if day == "Monday":
        return cardio[2:7]
    elif day == "Thursday":
        return cardio[4:10]
    else:
        return cardio[3:9]


def backWorkouts(level, day):
    lats = exercises.getExercise("lats", level)
    lower_back = exercises.getExercise("lower_back", level)
    middle_back = exercises.getExercise("middle_back", level)

    return lats[1:3] + lower_back[5:7] + middle_back[2:5]


def chestWorkouts(level, day):
    chest = exercises.getExercise("chest", level)

    return chest[2:8]


def armWorkouts(level, day):
    biceps = exercises.getExercise("biceps", level)
    triceps = exercises.getExercise("triceps", level)

    if day == "Tuesday":
        return biceps[3:7] + triceps[2:6]
    else:
        return biceps[2:5] + triceps[7:10]


def shoulderWorkouts(level, day):
    neck = exercises.getExercise("neck", level)
    traps = exercises.getExercise("traps", level)
    forearms = exercises.getExercise("forearms", level)

    return neck[0:2] + traps[4:7] + forearms[7:10]


def lowerWorkouts(level, day):
    calves = exercises.getExercise("calves", level)
    quads = exercises.getExercise("quadriceps", level)
    glutes = exercises.getExercise("glutes", level)
    hams = exercises.getExercise("hamstrings", level)
    adds = exercises.getExercise("adductors", level)

    wednesday = quads[0:2] + glutes[0:2] + hams[3:5] + adds[0:2] + calves[0:2]
    friday = quads[3:5] + glutes[2:4] + hams[1:3] + adds[2:4] + calves[3:5]

    if day == "Wednesday":
        return wednesday
    else:
        return friday


def abWorkouts(level, day):
    abs = exercises.getExercise("abdominals", level)

    if day == "Thursday":
        return abs[3:8]
    else:
        return abs[4:10]


def athleticFit(level):
    for day in plan:

        if day == "Sunday":
            print(day + " - " + plan[day] + "\n")
            continue

        muscle1 = plan[day].rstrip().split(' + ')[0].lower()
        muscle2 = plan[day].rstrip().split(' + ')[1].lower()
        print(day + " - " + plan[day] + "\n")

        if muscle1 == "cardio":
            print("---CARDIO---")
            printWorkout(cardioWorkouts(level,day))
        elif muscle1 == "arms":
            print("---ARMS---")
            printWorkout(armWorkouts(level,day))
        elif muscle1 == "lower":
            print("---LOWER (LEGS + THIGHS + CALVES)---")
            printWorkout(lowerWorkouts(level,day))

        if muscle2 == "chest":
            print("---CHEST---")
            printWorkout(chestWorkouts(level,day))
        elif muscle2 == "back":
            print("---BACK---")
            printWorkout(backWorkouts(level,day))
        elif muscle2 == "shoulders":
            print("---SHOULDERS---")
            printWorkout(shoulderWorkouts(level,day))
        elif muscle2 == "abs":
            print("---ABS---")
            printWorkout(abWorkouts(level,day))
