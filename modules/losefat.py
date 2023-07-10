# Lose Fat Module of FitFreak
from modules import exercises

# Splits and Plans
split = ("Chest + Triceps", "Back + Biceps", "Cardio + Abs", "Shoulders + Biceps", "Upper + Abs", "Lower + Triceps")
plan = dict({"Monday": split[0], "Tuesday": split[1], "Wednesday": split[2], "Thursday": split[3], "Friday": split[4],
             "Saturday": split[5], "Sunday": "Rest"})


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

    return lats[1:3] + lower_back[6:8] + middle_back[1:4]


def shoulderWorkouts(level, day):
    neck = exercises.getExercise("neck", level)
    traps = exercises.getExercise("traps", level)
    forearms = exercises.getExercise("forearms", level)

    return neck[0:2] + traps[3:6] + forearms[5:7]


def lowerWorkouts(level, day):
    calves = exercises.getExercise("calves", level)
    quads = exercises.getExercise("quadriceps", level)
    glutes = exercises.getExercise("glutes", level)
    hams = exercises.getExercise("hamstrings", level)
    adds = exercises.getExercise("adductors", level)

    return quads[3:5] + glutes[2:4] + hams[4:6] + adds[2:4] + calves[3:5]


def chestWorkouts(level, day):
    chest = exercises.getExercise("chest", level)

    return chest[2:7]


def tricepsWorkouts(level, day):
    triceps = exercises.getExercise("triceps", level)

    return triceps[1:4]


def bicepsWorkouts(level, day):
    biceps = exercises.getExercise("biceps", level)

    return biceps[2:6]


def upperWorkouts(level, day):
    chest = exercises.getExercise("chest", level)[3:6]
    back = exercises.getExercise("lats", level)[8:10] + exercises.getExercise("lower_back", level)[
                                                        7:9] + exercises.getExercise("middle_back", level)[5:7]

    return chest + back


def abWorkouts(level, day):
    abs = exercises.getExercise("abdominals", level)

    if day == "Wednesday":
        return abs[0:5]
    else:
        return abs[5:10]


def cardioWorkouts(level, day):
    cardio = exercises.getExerciseType("cardio", level)

    return cardio


# Lose Fat Plan
def loseFat(level):
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
        elif muscle1 == "cardio":
            print("---CARDIO---")
            printWorkout(cardioWorkouts(level, day))
        elif muscle1 == "shoulders":
            print("---SHOULDERS---")
            printWorkout(shoulderWorkouts(level, day))
        elif muscle1 == "upper":
            print("---UPPER BODY---")
            printWorkout(upperWorkouts(level, day))
        elif muscle1 == "lower":
            print("---LOWER (LEGS + THIGHS + CALVES)---")
            printWorkout(lowerWorkouts(level, day))

        if muscle2 == "abs":
            print("---ABS---")
            printWorkout(abWorkouts(level, day))
        elif muscle2 == "triceps":
            print("---TRICEPS--- ")
            printWorkout(tricepsWorkouts(level, day))
        elif muscle2 == "biceps":
            print("---BICEPS--- ")
            printWorkout(bicepsWorkouts(level, day))
