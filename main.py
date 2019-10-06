import time
from methods.random_restart import random_restart
from methods.steepest import steepest
from methods.first_choice import first_choice
from methods.simulated_annealing import simulated_annealing
from tools.graph import my_bar_chart

with open("./cases.txt", "r") as f:
    instances = f.read().split("\n")
    cases = []  # convert the cases into tuple type
    for instance in instances[:-1]:
        cases.append([int(pos) for pos in instance.split()])

time_cut_0 = time.clock()

# for steepest
steepest_solved_num = 0
for case in cases:
    if steepest(case):
        steepest_solved_num += 1
time_cut_1 = time.clock()
print("==steepest finished==")
steepest_time = time_cut_1 - time_cut_0
steepest_per = steepest_solved_num *100 / 400

# for first_choice
first_choice_solved_num = 0
for case in cases:
    if first_choice(case):
        first_choice_solved_num += 1
time_cut_2 = time.clock()
print("==first choice finished==")
first_choice_time = time_cut_2 - time_cut_1
first_choice_per = first_choice_solved_num * 100 / 400

# for random_restart
random_restart_solved_num = 0
for case in cases:
    if random_restart(case):
        random_restart_solved_num += 1
time_cut_3 = time.clock()
print("==random restart finished==")
random_restart_time = time_cut_3 - time_cut_2
random_restart_per = random_restart_solved_num * 100 / 400

# for simulated_annealing
simulated_annealing_solved_num = 0
for case in cases:
    if simulated_annealing(case):
        simulated_annealing_solved_num += 1
time_cut_4 = time.clock()
print("==simulated_annealing finished==")
simulated_annealing_time = time_cut_4 - time_cut_3
simulated_annealing_per = simulated_annealing_solved_num * 100 / 400

algs_list = ["steepest", "first-choice", "random-restart", "simulated-annealing"]
time_list = [steepest_time, first_choice_time, random_restart_time, simulated_annealing_time]
solved_per_list = [steepest_per, first_choice_per, random_restart_per, simulated_annealing_per]

# just for test
print(time_list)
print(solved_per_list)

my_bar_chart("Time consumption comparison", "Algorithms", "Time(seconds)", algs_list, time_list)
my_bar_chart("Solved percentage comparison", "Algorithms", "percentage(%)", algs_list, solved_per_list)

