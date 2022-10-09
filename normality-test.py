# normality testing and or plotting imports
import matplotlib.pyplot as plt

# open crossframe seeds file
f = open("outputs/crossframe_seeds_output.txt", "r")

# read all crossframe seeds
seeds = f.readlines()

# traverse through all seeds and load in memory (as int)
seed_array = []
for seed in seeds:
    seed_array.append(int(seed))

# create histogram
plt.hist(seed_array, edgecolor="black", bins=100)
plt.show()
