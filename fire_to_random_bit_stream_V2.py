# video processing, timing, and hashlib import
import cv2
import hashlib
import time

# open file to write random bit stream to
f = open("outputs/random-bit-stream.txt", "w")

# hex to binary function definition
def hex_to_bin(h):
  return bin(int(h, 16))[2:].zfill(len(h) * 4)

# open video stream of webcam
vid = cv2.VideoCapture(0)

# make sure that webcam opened properly
if vid.isOpened() is False :
  print("Exiting: Cannot access webcam stream!")
  exit(0)

# loop through frames in video file, storing each frames pixel seeds
frameSeedsArray = []
frameCount = 0
start_true_time = time.perf_counter() # start timer for true random portion
while (True):
    # initialize this frames seeds array
    seeds = []
    # read the current frame, get its dimensions
    success, frame = vid.read()
    rows, cols, _ = frame.shape
    # iterate over frames pixels, skipping four each step to avoid patterns
    for i in range(rows):
        if i % 4 != 0:
            continue
        for j in range(cols):
            if j % 4 != 0:
                continue
            # extract and test weather this pixel is within an "orange fire" range
            b, g, r = frame[i, j]
            if (120 <= r) and (20 <= g <= 160) and (0 <= b <= 70):
                # write seed for this pixel to seeds array
                hashIngest = format(r, '03d') + format(int(i/4), '03d') + format(g, '03d') + format(int(j/4), '03d') + format(b, '02d')
                seeds.append(hashIngest)
    # store seeds array (consisting of pixel seeds in md5 hex form) for this frame
    frameSeedsArray.append(seeds)
    # show and increment frame counter, display seed count
    print('FINISHED FRAME: ' + str(frameCount) + " WITH " + str(len(seeds)) + " FIRE PIXEL SEEDS")
    frameCount += 1
    # stop when 144 frames have been captured
    if frameCount == 144:
        break
# end timer for true random portion and display time taken
end_true_time = time.perf_counter()
print(f"Finished true random portion in {end_true_time - start_true_time:0.4f} seconds")

# loop through all frame seeds now that they are in memory
start_psuedo_time = time.perf_counter() # start timer for psuedo random portion
for i in range(len(frameSeedsArray) - 12):
    # load this frames seeds and 4/8/12 frames ahead seeds 
    a = frameSeedsArray[i]
    b = frameSeedsArray[i+4]
    c = frameSeedsArray[i+8]
    d = frameSeedsArray[i+12]
    # find which frame has the least seeds,
    # this will determine the amount of cross-frame seeds we make for this set of four
    size = min(len(a), len(b), len(c), len(d))
    # perform mixed cross-frame hash operation on pixel seeds to create and write final seeds
    for i in range(size):
        hashIngest = ((hashlib.md5(a[i].encode('utf-8')).hexdigest()) + (hashlib.md5(b[size - 1 - i].encode('utf-8')).hexdigest()) + 
                        (hashlib.md5(c[i].encode('utf-8')).hexdigest()) + (hashlib.md5(d[size - 1 - i].encode('utf-8')).hexdigest()))
        hashResultHex = hashlib.sha512((hashIngest).encode('utf-8')).hexdigest()
        # write final seeds data as a ascii binary stream
        f.write(hex_to_bin(hashResultHex))
# end timer for true random portion and display time taken
end_psuedo_time = time.perf_counter()
print(f"Finished psuedo random portion in {end_psuedo_time - start_psuedo_time:0.4f} seconds")

# close random bit stream file
f.close()
