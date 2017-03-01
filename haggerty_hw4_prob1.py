# Author: Parker Haggerty
# Date: 2/27/17
# Assignment 4, Problem 1


# Import stuff
import math
from matplotlib import pyplot as p
import random


# Constants
Bi213 = 10000      #Number of Bi213 atoms
Bi209 = 0           #Number of Bi209 atoms
Tl = 0              #Number of Tl209 atoms
Pb = 0              #Number of Pb209 atoms
tmax = 20000        #Total (max) time


# Probability
probability_Pb =(1 - .9965)
probability_Tl = (1 - .9948)
probability_Bi = (1 - .9997)


# Data
Bi213_points = []
Tl_points = []
Pb_points = []
Bi209_points = []


# Main Loop (for reference, consult page 455 in book)
for t in range(tmax):
    Bi213_points.append(Bi213)
    Tl_points.append(Tl)
    Pb_points.append(Pb)
    Bi209_points.append(Bi209)
    
    for s in range(Pb):
        Pb_decay = 0
        if random.uniform(0,1)< probability_Pb:
            Pb_decay += 1
        Pb -= Pb_decay
        Bi209 += Pb_decay
    
    for s in range(Tl):
        Tl_decay = 0
        if random.uniform(0,1)<probability_Tl:
            Tl_decay += 1
        Tl -= Tl_decay
        Pb += Tl_decay
        
    for s in range(Bi213):
        Bi2Tl_decay = 0
        Bi2Pb_decay = 0
        
        if random.uniform(0,1)<0.9791:
            if random.uniform(0,1)< probability_Bi:
                Bi2Pb_decay += 1
            Pb += Bi2Pb_decay
            Bi213 -= Bi2Pb_decay
        else:
            if random.uniform(0,1)< probability_Bi:
                Bi2Tl_decay += 1
            Tl += Bi2Tl_decay
            Bi213 -= Bi2Tl_decay

# Graph           
p.title("Bi_213 Decay Over Time")
p.xlabel("Time (sec)")
p.ylabel("# of atoms")
p.plot(range(tmax), Bi213_points, '#ffc61a', label="Bi_213")
p.plot(range(tmax), Tl_points, '#1aff53', label="Tl_209")
p.plot(range(tmax), Pb_points, '#1ac6ff', label="Pb_209")
p.plot(range(tmax), Bi209_points, '#531aff', label="Bi_209")
p.legend()
p.savefig("Bi_213DecayOverTime.png")
p.show()
        