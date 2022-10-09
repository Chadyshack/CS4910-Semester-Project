# open frame seeds file
f = open("frame_seeds_output.txt", "r")

# open crossframe seeds file
c = open("crossframe_seeds_output.txt", "w")

# read all lines of frame seeds file
frames = f.readlines()

# loop through all frames
frame_seeds_array = []
for frame in frames:
    # extract this frames seeds into array
    frame_seeds = frame.split(",")
    # remove breakline on final element
    frame_seeds[-1] = frame_seeds[-1].strip()
    # append to the frame seeds array
    frame_seeds_array.append(frame_seeds)

print(frame_seeds_array)
