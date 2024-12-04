import random
from Project.algorithms.fitness_function import fitness_function

def crossover(parent1, parent2):
    split_point = len(parent1) // 2
    child1 = parent1[:split_point] + [
        session for session in parent2[split_point:] if is_valid(session, parent1[:split_point])
    ]
    child2 = parent2[:split_point] + [
        session for session in parent1[split_point:] if is_valid(session, parent2[:split_point])
    ]
    return child1, child2

def is_valid(session, partial_timetable):
    _, lecturer_id, day, timeslot, room_id = session

    if any(s[4] == room_id and s[2] == day and s[3] == timeslot for s in partial_timetable):
        return False

    if any(s[1] == lecturer_id and s[2] == day and s[3] == timeslot for s in partial_timetable):
        return False

    return True

def mutate(timetable, rooms):
    if len(timetable) > 0:
        idx = random.randint(0, len(timetable) - 1)
        mutated_session = timetable[idx]
        _, lecturer_id, day, timeslot, room_id = mutated_session

        room = random.choice(rooms)
        day, timeslot = random.choice([
        ("Sunday", "08:00-9:00"), ("Sunday", "9:00-10:00"),("Sunday", "10:00-11:00"),("Sunday", "11:00-12:00"),
        ("Monday", "08:00-9:00"), ("Monday", "9:00-10:00"),("Monday", "10:00-11:00"),("Monday", "11:00-12:00"),
        ("Tuesday", "08:00-9:00"), ("Tuesday", "9:00-10:00"),("Tuesday", "10:00-11:00"),("Tuesday", "11:00-12:00"),
        ("Wednesday", "08:00-9:00"), ("Wednesday", "9:00-10:00"),("Wednesday", "10:00-11:00"),("Wednesday", "11:00-12:00"),
        ("Thursday", "08:00-9:00"), ("Thursday", "9:00-10:00"),("Thursday", "10:00-11:00"),("Thursday", "11:00-12:00"),
        ])

        new_session = (mutated_session[0], lecturer_id, day, timeslot, room["id"])

        if is_valid(new_session, timetable[:idx] + timetable[idx+1:]):
            timetable[idx] = new_session

def genetic_algorithm(population, generations, mutation_rate, rooms):
    for _ in range(generations):
        population = sorted(population, key=fitness_function, reverse=True)
        new_population = []

        for i in range(len(population) // 2):
            parent1, parent2 = population[i], population[i + 1]
            child1, child2 = crossover(parent1, parent2)

            if random.random() < mutation_rate:
                mutate(child1, rooms)
            if random.random() < mutation_rate:
                mutate(child2, rooms)

            new_population.extend([child1, child2])

        population = new_population

    # Return the best solution
    return population[0]