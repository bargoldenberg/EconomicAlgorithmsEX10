import math
#IMPLEMENTED BY: BAR GOLDENBERG.

def f(i, t, C):
    return C*min(1,(i+1)*t) # i is an index so it starts at 0 in python so if f_i(1) = C, i is atleast 1. 

def calc_t_budget(total_budget: float, citizen_votes: list[list[float]], t: float) -> list[float]:
    budget = []
    amount_of_subjects = len(citizen_votes[0])
    amount_of_citizens = len(citizen_votes)
    for subject in range(amount_of_subjects):
            subject_votes = []
            subject_votes = [citizen_votes[citizen][subject] for citizen in range(amount_of_citizens)]
            # create n-1 functions
            for i in range(amount_of_citizens - 1):
                subject_votes.append(f(i,t,total_budget))
            # sort values to choose median
            subject_votes.sort()
            # get median value
            budget.append(subject_votes[math.floor((len(subject_votes)-1)/2)])
    return budget

def compute_budget(total_budget: float, citizen_votes: list[list[float]]) -> list[float]:
    t_min = 0
    t_max = 1
    t = 0.5
    budget = []
    #binary search to find correct t.
    while sum(budget) != total_budget:
        budget = calc_t_budget(total_budget, citizen_votes, t)
        if sum(budget) > total_budget:
            t_max = t
            t = (t_min + t) / 2
        else:
            t_min = t
            t = (t_max + t) / 2
    return budget

# TESTS
total_budget = 100
citizen_votes = [[100, 0, 0], [0, 0, 100]]
assert(compute_budget(total_budget, citizen_votes) == [50.0, 0, 50.0])

total_budget = 30
citizen_votes = [[6, 6, 6, 6, 0, 0, 6, 0, 0], [0, 0, 6, 6, 6, 6, 0, 6, 0], [6, 6, 0, 0, 6, 6, 0, 0, 6]]
assert(compute_budget(total_budget, citizen_votes) == [4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 2.0, 2.0, 2.0])

total_budget = 99
citizen_votes = [[33, 33, 33], [33, 33, 33]]
assert(compute_budget(total_budget, citizen_votes) == [33, 33, 33])