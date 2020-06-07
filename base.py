import random

workout_list = [
    {"name" : "workout name - 1", "duration" : 2},
    {"name" : "workout name - 2", "duration" : 4},
    {"name" : "workout name - 3", "duration" : 2},
    {"name" : "workout name - 4", "duration" : 4},
    {"name" : "workout name - 5", "duration" : 2},
    {"name" : "workout name - 6", "duration" : 4},
    {"name" : "workout name - 7", "duration" : 2},
    {"name" : "workout name - 8", "duration" : 2},
    {"name" : "workout name - 9", "duration" : 4}
]
done_workout = []
total_workout = []
total_time = 0

def generate_random_numbers(min, max):
    return random.randint(min,max)

def start():
    global total_time
    number = -1
    if (total_time < 150):
        number = generate_random_numbers(0,8)
        if (len(done_workout)) == 0:
            done_workout.append(number) 
        else:
            print("here")
            print(number)
            print(done_workout)
            if (number in done_workout ):
                start()
            else:
                done_workout.append(number)
        random_number = generate_random_numbers(7,15)
        total_time = total_time + (workout_list[number]["duration"] * random_number)
        add_routine = workout_list[number]
        add_routine["reps"] = random_number
        total_workout.append(add_routine)
        start()
    else:
        print(total_workout)
        print("time of workout " + str(total_time))
        exit()


start()