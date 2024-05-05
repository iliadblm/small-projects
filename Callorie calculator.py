age_r = False
gender_r = False
height_r = False
weight_r = False
activities_r = False

while not age_r:
    try:
        age = input("Insert your age:   ")
        age = int(age)
        if 13 <= age <= 80:
            age_r = True
        else:
            print("[Wrong age, try again]\n")
    except ValueError:
        print("[Wrong age, try again]\n")


while not gender_r:
    try:
        gen = 0
        gender = input("\nChoose your gender, male or female:  \n1 - Male  \n2 - Female\n")
        gender = int(gender)
        if gender == 1:
            gender_r = True
            gen = 1
        elif gender == 2:
            gender_r = True
            gen = 2
        else:
            print("[Wrong gender, try again]\n")
    except ValueError:
        print("[Wrong gender, try again]\n")


while not height_r:
    try:
        height = input("\nInsert your height in centimeters:   ")
        height = float(height)
        if 100 <= height <= 300:
            height_r = True
        else:
            print("[Wrong height, try again]\n")
    except ValueError:
        print("[Wrong height, try again]\n")


while not weight_r:
    try:
        weight = input("\nInsert your weight in kilograms:   ")
        weight = float(weight)
        if 30 <= weight <= 200:
            weight_r = True
        else:
            print("[Wrong weight, try again]\n")
    except ValueError:
        print("[Wrong weight, try again]\n")


while not activities_r:
    try:
        act = 0
        activities = input("\nChoose your level of activities:\n1 - Minimal\n2 - Weak\n3 - Middle\n4 - High\n5 - Extra\n")
        activities = int(activities)
        if activities == 1:
            activities_r = True
            act = 1.2
        elif activities == 2:
            activities_r = True
            act = 1.375
        elif activities == 3:
            activities_r = True
            act = 1.55
        elif activities == 4:
            activities_r = True
            act = 1.725
        elif activities == 5:
            activities_r = True
            act = 1.9
        else:
            print("[Wrong level of activities, try again]\n")
    except ValueError:
        print("[Wrong level of activities, try again]\n")


def count_the_energy_value():
    global total_c
    if gen == 1:
        total_c = ((10 * weight) + (6.25 * height) - (5 * age) + 5) * act
    elif gen == 2:
        total_c = ((10 * weight) + (6.25 * height) - (5 * age) - 161) * act
    print(total_c)


print(count_the_energy_value())
