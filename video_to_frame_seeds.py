# video processing import
import cv2

# open video file of fire
vid = cv2.VideoCapture("burning-charcoal-fire.mp4")

# open file to write seed to
f = open("frame_seeds_output.txt", "w")

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
            if (120 <= r) and (20 <= g <= 160) and (5 <= b <= 70):
                # write "orange" pixels and their locations to random string (after multiplication operations test)
                rand += (str(((r + i) * (g + j)) * b) + ",")
    # store random string for this frame, show and increment frame counter
    f.write(rand[:-1] + '\n')
    print('ON FRAME: ' + str(frameCount))
    frameCount += 1
    # exit when end of video reached
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# close seed file
f.close()
