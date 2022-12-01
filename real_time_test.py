import cv2
import time

# open video stream
vcap = cv2.VideoCapture(0)

# make sure that it opened properly
if vcap.isOpened() is False :
  print("[Exiting]: Error accessing webcam stream.")
  exit(0)

# check fps of video and read first frame to warm hardware
fps_input_stream = int(vcap.get(5))
print("FPS of input stream{}".format(fps_input_stream))
grabbed, frame = vcap.read()

# start processing
num_frames_processed = 0 
start = time.time()
while True :
    grabbed, frame = vcap.read()
    if grabbed is False :
        print('[Exiting] No more frames to read')
        break
    # adding a delay for simulating video processing time 
    delay = 0.03
    time.sleep(delay) 
    num_frames_processed += 1
    # displaying frame 
    cv2.imshow('frame' , frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
end = time.time()

# printing time elapsed and fps 
elapsed = end-start
fps = num_frames_processed/elapsed 
print("FPS: {} , Elapsed Time: {} ".format(fps, elapsed))
# releasing input stream, closing all windows 
vcap.release()
cv2.destroyAllWindows()
