# open frame seeds file
f = open("frame_seeds_output.txt", "r")

# open crossframe seeds file
c = open("crossframe_seeds_output.txt", "w")

# read all lines of frame seeds file
frames = f.readlines()

# loop through all frames from frame seeds file
frame_seeds_array = []
for frame in frames:
    # extract this frames seeds into array
    frame_seeds = frame.split(",")
    # remove breakline on final element
    frame_seeds[-1] = frame_seeds[-1].strip()
    # convert all strings to integers
    frame_seeds_final = [eval(i) for i in frame_seeds]
    # append to the frame seeds array
    frame_seeds_array.append(frame_seeds_final)

# loop through all frame seeds now that they are in memory and integer form (stop 3 early to handle for 3 frame lookahead)
for i in range(len(frame_seeds_array) - 3):
    # load this frames seeds and 3 frames ahead seeds
    a = frame_seeds_array[i]
    b = frame_seeds_array[i+3]
    # find which frame had less seeds
    size = min(len(a), len(b))
    # multiply all seeds in a backwards pattern and store each seed
    for i in range(size):
        c.write(str(a[i] * b[size - 1 - i]) + '\n')

# close both files
f.close()
c.close()
