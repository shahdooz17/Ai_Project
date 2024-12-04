import random
from Project.Data.courses import courses
from Project.Data.lecturers import lecturers
from Project.Data.rooms import rooms

def generate_initial_population(num_individuals):
    timeslots = [
        ("Sunday", "08:00-9:00"), ("Sunday", "9:00-10:00"),("Sunday", "10:00-11:00"),("Sunday", "11:00-12:00"),
        ("Monday", "08:00-9:00"), ("Monday", "9:00-10:00"),("Monday", "10:00-11:00"),("Monday", "11:00-12:00"),
        ("Tuesday", "08:00-9:00"), ("Tuesday", "9:00-10:00"),("Tuesday", "10:00-11:00"),("Tuesday", "11:00-12:00"),
        ("Wednesday", "08:00-9:00"), ("Wednesday", "9:00-10:00"),("Wednesday", "10:00-11:00"),("Wednesday", "11:00-12:00"),
        ("Thursday", "08:00-9:00"), ("Thursday", "9:00-10:00"),("Thursday", "10:00-11:00"),("Thursday", "11:00-12:00"),
    ]
    population = []

    for _ in range(num_individuals):
        timetable = []
        used_slots = set()  # To prevent overlapping rooms and lecturers

        for course in courses:
            valid = False
            while not valid:
                lecturer = random.choice(lecturers)
                room = random.choice(rooms)
                day, timeslot = random.choice(timeslots)

                if (room["id"], day, timeslot) in used_slots or (lecturer["id"], day, timeslot) in used_slots:
                    continue

                if (day, timeslot) in lecturer["unavailable"]:
                    continue

                if course["students"] > room["capacity"]:
                    continue

                timetable.append((course["name"], lecturer["name"], day, timeslot, room["id"]))
                used_slots.add((room["id"], day, timeslot))
                used_slots.add((lecturer["name"], day, timeslot))
                valid = True

        population.append(timetable)

    return population