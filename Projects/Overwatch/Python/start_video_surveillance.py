## TODO
## Make change means dynamic for each area.
## Take the average of the last .. 50? frames

print("Importing dependencies.. ")
import sys
import time
import datetime
from SimpleCV import *
from image_utils import *
import numpy as np
import cv2

MOTION_INTERVAL = 0.1
DURATION = 300
RAMP_FRAMES = 30

if __name__ == "__main__":

    # Initial Steps #
    fourcc = cv2.cv.CV_FOURCC(*'XVID')
    v = cv2.VideoCapture(-1)

    # Ramp-up Camera
    print("Ramping up camera..")
    for i in xrange(RAMP_FRAMES):
        ret, img = v.read()

    # Writer
    initial_pic_path = os.path.join(PIC_PATH, 'initial.png')
    print(initial_pic_path)
    #vo = cv2.VideoWriter(initial_pic_path, fourcc, 20.0, FOUR_EIGHTY_RESOLUTION)
    #vo = cv2.VideoWriter(initial_pic_path, fourcc, 20.0, SEVEN_TWENTY_RESOLUTION)
    
    # Clear contents of Picture folder
    clear_picture_folder()

    # Stuff
    START_TIME = time.time()
    current_time = 0

    # Take initial picture
    (ret, INITIAL_FRAME) = v.read()
    cv2.imwrite(initial_pic_path, INITIAL_FRAME)
    
    # Crop desired AOIs
    INITIAL_INTERSECTION = crop_initial_video(INITIAL_FRAME, [IC_X1, IC_X2, IC_Y1, IC_Y2], INTERSECTION_NAME, write=True)
    INITIAL_ROAD_LEFT = crop_initial_video(INITIAL_FRAME, [RLC_X1, RLC_X2, RLC_Y1, RLC_Y2], ROAD_LEFT_NAME, write=True)
    INITIAL_ROAD_FRONT = crop_initial_video(INITIAL_FRAME, [RFC_X1, RFC_X2, RFC_Y1, RFC_Y2], ROAD_FRONT_NAME, write=True)

    # Iterate for specified duration
    while current_time - START_TIME <= DURATION:
        time.sleep(MOTION_INTERVAL)

        # Set current time
        current_time = time.time()
        time_stamp = datetime.utcnow()

        # Get current frame
        print("Taking picture at {}..".format(time_stamp))
        ret, current_frame = v.read()
        current_intersection = crop_initial_video(current_frame, [IC_X1, IC_X2, IC_Y1, IC_Y2], INTERSECTION_NAME)
        current_road_left = crop_initial_video(current_frame, [RLC_X1, RLC_X2, RLC_Y1, RLC_Y2], ROAD_LEFT_NAME)
        current_road_front = crop_initial_video(current_frame, [RFC_X1, RFC_X2, RFC_Y1, RFC_Y2], ROAD_FRONT_NAME)

        # Compare metrics
        intersection_diff = INITIAL_INTERSECTION - current_intersection
        road_left_diff = INITIAL_ROAD_LEFT - current_road_left
        road_front_diff = INITIAL_ROAD_FRONT - current_road_front

        #intersection_matrix = intersection_diff.getNumpy()
        #road_left_matrix = road_left_diff.getNumpy()
        #road_front_matric = road_front_diff.getNumpy()
       
        intersection_mean = intersection_diff.mean()    
        print("Intersection: {}".format(intersection_mean))
        road_left_mean = road_left_diff.mean()
        print("Road Left: {}".format(road_left_mean))
        road_front_mean = road_front_diff.mean()
        print("Road Front: {}".format(road_front_mean))
 
        if road_left_mean >= 50  or intersection_mean >= 50 or road_front_mean >= 50:
            print("Motion detected! Starting recording..")
            current_time = DURATION + 50000

            # Shoot dat video
            try:
                vid = take_a_video(v, 10, 20, PIC_PATH)
            except Exception as err:
                raise(err)
            time.sleep(0.5)
            
            # If video capture finished successfully
            if vid == 0:
                current_time = time.time() - START_TIME
            #current_time = time.time() - START_TIME
                
                
    print("Complete!")	
