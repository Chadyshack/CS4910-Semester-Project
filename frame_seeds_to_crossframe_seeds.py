# import hashlib
import hashlib

# hex to binary function definition
def hex_to_bin(h):
  return bin(int(h, 16))[2:].zfill(len(h) * 4)

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
    # remove final element (break line)
    del(frame_seeds[-1])
    # append to the frame seeds array
    frame_seeds_array.append(frame_seeds)

# loop through all frame seeds now that they are in memory, ensure there is at least 13 frames to preform lookahead
if len(frame_seeds_array) < 13:
    raise Exception
for i in range(len(frame_seeds_array) - 12):
    # load this frames seeds and 4/8/12 frames ahead seeds 
    a = frame_seeds_array[i]
    b = frame_seeds_array[i+4]
    c = frame_seeds_array[i+8]
    d = frame_seeds_array[i+12]
    # find which frame has the least seeds, this will determine the amount of cross-frame seeds we make
    size = min(len(a), len(b), len(c), len(d))
    # perform mixed cross-frame hash operation on pixel seeds to create and write final seeds
    for i in range(size):
        hashIngest = a[i] + b[size - 1 - i] + c[i] + d[size - 1 - i]
        hashResultHex = hashlib.sha256((hashIngest).encode('utf-8')).hexdigest()
        # write final seeds data as a ascii binary stream
        cross.write(hex_to_bin(hashResultHex))

# close both files
f.close()
cross.close()
