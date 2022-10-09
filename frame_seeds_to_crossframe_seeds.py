# open frame seeds file
f = open("frame_seeds_output.txt", "r")

# open crossframe seeds file
c = open("crossframe_seeds_output.txt", "r")

# read all lines of frame seeds file
frames = f.readlines()

# loop through all frame seeds and store in array
frame_array = []
for frame in frames:
    frame_array.append(frame.split(","))

print(frame_array)
