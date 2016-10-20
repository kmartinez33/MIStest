import random

ROSTER = {"Beshansky": 0,
          "Collins": 0,
          "Fischer": 1,
          "Giovanucci": 0,
          "Jain": 0,
          "Kim": 0,
          "Lauture": 0,
          "Lee": 0,
          "Maddox": 0,
          "Martinez": 0,
          "Mendez": 0,
          "Oh": 0,
          "Petrone": 1,
          "Posada": 0,
          "Rule": 1,
          "Schilb": 0,
          "Tariq": 0,
          "Wang": 0,
          "Wolf": 0}


def call(roster):
    """
    Among the names that are called least times,
    print one name
    roster: a dict of names and integers
    """
    value_list = roster.values()
    min_value = min(value_list)

    temp_dict = dict() # this is the same as {}
    for name, number in roster.items(): # () indicates that it will be a fucntion and it  a dictionary there is ALWAYS a key and a value (name, number)
        if number == min_value:
            name.append(name)

    return random.choice(name)

call(ROSTER)