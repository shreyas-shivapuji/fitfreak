# Build Muscle module of FitFreak
from modules import exercises

# Bold Color ANSI Escape Sequence

# Motivation for muscle building here


# Workout plan for muscle building:
split = ("Chest + Triceps", "Back + Biceps", "Shoulders + Lower")
plan = dict({"Monday": split[0], "Tuesday": split[1], "Wednesday": split[2], "Thursday": split[0], "Friday": split[1],
             "Saturday": split[2], "Sunday": "Rest"})


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
def backWorkouts(level, day):
    lats = exercises.getExercise("lats", level)
    lower_back = exercises.getExercise("lower_back", level)
    middle_back = exercises.getExercise("middle_back", level)

    tuesday = lats[0:2] + lower_back[0:2] + middle_back[0:2]
    friday = lats[2:4] + lower_back[2:4] + middle_back[2:4]

    if day == "Tuesday":
        return tuesday
    else:
        return friday


def shoulderWorkouts(level, day):
    neck = exercises.getExercise("neck", level)
    traps = exercises.getExercise("traps", level)
    forearms = exercises.getExercise("forearms", level)

    wednesday = neck[0:2] + traps[0:2] + forearms[0:2]
    saturday = neck[2:4] + traps[2:4] + forearms[2:4]

    if day == "Wednesday":
        return wednesday
    else:
        return saturday


def lowerWorkouts(level, day):
    calves = exercises.getExercise("calves", level)
    quads = exercises.getExercise("quadriceps", level)
    glutes = exercises.getExercise("glutes", level)
    hams = exercises.getExercise("hamstrings", level)
    adds = exercises.getExercise("adductors", level)

    wednesday = quads[0:2] + glutes[0:2] + hams[3:5] + adds[0:2] + calves[0:2]
    saturday = quads[3:5] + glutes[2:4] + hams[1:3] + adds[2:4] + calves[3:5]

    if day == "Wednesday":
        return wednesday
    else:
        return saturday


def chestWorkouts(level, day):
    chest = exercises.getExercise("chest", level)

    if day == "Monday":
        return chest[0:5]
    else:
        return chest[5:10]


def tricepsWorkouts(level, day):
    triceps = exercises.getExercise("triceps", level)

    if day == "Monday":
        return triceps[0:5]
    else:
        return triceps[5:10]


def bicepsWorkouts(level, day):
    biceps = exercises.getExercise("biceps", level)

    if day == "Tuesday":
        return biceps[0:5]
    else:
        return biceps[5:10]


# Build Muscle Plan
def buildMuscle(level):
    for day in plan:

        if day == "Sunday":
            print(day + " - " + plan[day])
            continue

        muscle1 = plan[day].rstrip().split(' + ')[0].lower()
        muscle2 = plan[day].rstrip().split(' + ')[1].lower()
        print(day + " - " + plan[day] + "\n")
        if muscle1 == "chest":
            print("---CHEST---")
            printWorkout(chestWorkouts(level, day))
        elif muscle1 == "back":
            print("---BACK---")
            printWorkout(backWorkouts(level, day))
        elif muscle1 == "shoulders":
            print("---SHOULDERS---")
            printWorkout(shoulderWorkouts(level, day))

        if muscle2 == "lower":
            print("---LOWER (LEGS + THIGHS + CALVES)---")
            printWorkout(lowerWorkouts(level, day))
        elif muscle2 == "triceps":
            print("---TRICEPS--- ")
            printWorkout(tricepsWorkouts(level, day))
        elif muscle2 == "biceps":
            print("---BICEPS--- ")
            printWorkout(bicepsWorkouts(level, day))



