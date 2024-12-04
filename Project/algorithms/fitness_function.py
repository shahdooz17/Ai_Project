from Project.Data.courses import courses
from Project.Data.lecturers import lecturers
from Project.Data.rooms import rooms

def fitness_function(timetable):
    score = 0
    room_time_slots = set()  
    lecturer_time_slots = set()  

    for session in timetable:
        course_id, lecturer_id, day, timeslot, room_id = session
        course = next(c for c in courses if c["name"] == course_id)
        lecturer = next(l for l in lecturers if l["name"] == lecturer_id)
        room = next(r for r in rooms if r["id"] == room_id)

        if (day, timeslot) in lecturer["unavailable"]:
            continue

        if course["students"] > room["capacity"]:
            continue 

        if (room_id, day, timeslot) in room_time_slots:
            continue
        room_time_slots.add((room_id, day, timeslot))

        if (lecturer_id, day, timeslot) in lecturer_time_slots:
            continue
        lecturer_time_slots.add((lecturer_id, day, timeslot))

        score += 1

    return score