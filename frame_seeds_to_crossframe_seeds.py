# open frame seeds file
f = open("outputs/frame_seeds_output.txt", "r")

# open crossframe seeds file
cross = open("outputs/crossframe_seeds_output.txt", "w")

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

# loop through all frame seeds now that they are in memory and integer form
if len(frame_seeds_array) < 13:
    raise Exception
for i in range(len(frame_seeds_array) - 12):
    # load this frames seeds and 4/8/12 frames ahead seeds 
    a = frame_seeds_array[i]
    b = frame_seeds_array[i+4]
    c = frame_seeds_array[i+8]
    d = frame_seeds_array[i+12]
    # find which frame has the least seeds
    size = min(len(a), len(b), len(c), len(d))
    # perform cross-frame operation on seeds to create and write final seeds
    for i in range(size):
        cross.write(str(format(((a[i] + c[size - 1 - i]) * (b[i] + d[size - 1 - i])), "b"))) # SECOND GENERATION LOGIC

# close both files
f.close()
cross.close()
