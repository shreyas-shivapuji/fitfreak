import requests


def getExerciseType(type,level):
    url = "https://exercises-by-api-ninjas.p.rapidapi.com/v1/exercises"

    querystring = {"type": type}

    headers = {
        "X-RapidAPI-Key": "81ea64b741msh8b3c73653136f1cp1b3969jsn7cfb8485d2fa",
        "X-RapidAPI-Host": "exercises-by-api-ninjas.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()


def getExercise(muscle,level):
    url = "https://exercises-by-api-ninjas.p.rapidapi.com/v1/exercises"
    if level == "expert" : level = "intermediate"
    querystring = {"muscle": muscle, "difficulty": level}

    headers = {
        "X-RapidAPI-Key": "81ea64b741msh8b3c73653136f1cp1b3969jsn7cfb8485d2fa",
        "X-RapidAPI-Host": "exercises-by-api-ninjas.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()



