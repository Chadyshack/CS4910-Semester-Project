# video processing and hashlib import
import cv2
import hashlib

# open video file of fire
vid = cv2.VideoCapture("resources/burning-charcoal-fire.mp4")

# open file to write frame seeds to
f = open("outputs/frame_seeds_output.txt", "w")

# loop through frames in video file
frameCount = 0
while (True):
    # start this frames random bytes array
    rand = []
    # read the current frame, get its dimensions
    success, frame = vid.read()
    rows, cols, _ = frame.shape
    # iterate over frames pixels
    for i in range(rows):
        for j in range(cols):
            # extract and test weather this pixel is within an "orange fire" range
            b, g, r = frame[i, j]
            if (120 <= r) and (20 <= g <= 160) and (0 <= b <= 70):
                # write seed for this pixel to random bytes array
                hashIngest = format(r, '03d') + format(i, '04d') + format(g, '03d') + format(j, '04d') + format(b, '02d')
                # NOTE: There are 136 red, 141 green, 71 blue, 1080 i, and 1920 j possibilities for each value respectively,
                # this gives (136 * 141 * 71 * 1080 * 1920) = 2,823,198,105,600 possible pixel seeds!
                rand.append(hashlib.md5((hashIngest).encode('utf-8')))
    # store random bytes array (consisting of pixel seeds in md5 hex form) for this frame
    for seed in rand:
        f.write(seed.hexdigest() + ',')
    f.write('\n')
    # show and increment frame counter
    print('FINISHED FRAME: ' + str(frameCount) + " WITH " + str(len(rand)) + " FIRE PIXEL SEEDS")
    frameCount += 1
    # exit when 32 frames reached
    if frameCount == 32:
        break

# close seed file
f.close()
