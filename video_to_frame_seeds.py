# video processing import
import cv2

# open video file of fire
vid = cv2.VideoCapture("resources/burning-charcoal-fire.mp4")

# open file to write frame seeds to
f = open("outputs/frame_seeds_output.txt", "w")

# loop through frames in video file
frameCount = 0
while (True):
    # start this frames random string
    rand = ''
    # read the current frame, get its dimensions
    success, frame = vid.read()
    rows, cols, _ = frame.shape
    # iterate over frames pixels
    for i in range(rows):
        for j in range(cols):
            # extract and test weather this pixel is within an "orange" range
            b, g, r = frame[i, j]
            if (120 <= r) and (20 <= g <= 160) and (0 <= b <= 70):
                # write seed for this pixel to random string
                r = int(r)
                g = int(g)
                b = int(b)
                rand += (str(r*g*b) + ",")
    # store random string (consisting of seeds) for this frame, show and increment frame counter
    f.write(rand[:-1] + '\n')
    print('ON FRAME: ' + str(frameCount))
    frameCount += 1
    # exit when 100 frames reached
    if frameCount == 100:
        break

# close seed file
f.close()
