# video processing import
import cv2

# open video file of fire
vid = cv2.VideoCapture("burning-charcoal-fire.mp4")

# open file to write seed to
f = open("seed_output.txt", "w")

# loop through frames in video file
frameCount = 0
while (True):
    # read the current frame, get its dimensions
    success, frame = vid.read()
    rows, cols, _ = frame.shape
    # iterate over frames pixels
    for i in range(rows):
        for j in range(cols):
            # extract and test weather this pixel is within an "orange" range
            b, g, r = frame[i, j]
            if (180 <= r <= 240) and (70 <= g <= 120) and (20 <= b <= 50):
                # write "orange" pixels to seed file
                f.write("(" + str(r) + "," + str(g) + "," + str(b) + ")")
    # store, show, and count current frame
    f.write("\nDONE WITH FRAME: " + str(frameCount) + "\n")
    print("ON FRAME: " + str(frameCount))
    frameCount += 1
    # exit when end of video reached
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# close seed file
f.close()
