import tkinter as tk
from Project.algorithms.generate_intial_population import generate_initial_population
from Project.algorithms.genetic_algorithm import genetic_algorithm
from Project.Data.rooms import rooms

def run_algorithm():
    population = generate_initial_population(10)
    best_timetable = genetic_algorithm(population, generations=50 , mutation_rate=0.1,rooms=rooms)
    result_window = tk.Toplevel()
    result_window.title("Result")
    tk.Label(result_window,text="Best TimeTable:").pack()
    for session in best_timetable:
        tk.Label(result_window,text=str(session)).pack()

def get_user_interface():
    root = tk.Tk()
    root.title("Timetable Scheduler")

    tk.Label(root, text="TimeTable scheduling results").pack(pady=10)
    tk.Button(root,text="Run Scheduler",command=run_algorithm).pack(pady=20)

    root.mainloop()
