import os
import sys
import time
import cv2
import numpy as np
from SimpleCV import *
from datetime import datetime

# Constants
PNG_EXT = ".png"

# Initial picture constants
INITIAL_NAME = "_initial.png"

# Misc Constants
PIC_PATH = r"/home/pi/Pictures"
SEVEN_TWENTY_RESOLUTION = (1280, 720)
FOUR_EIGHTY_RESOLUTION = (640, 480)

def take_a_picture(c=None, write=False):
    # If there isn't a camera connection, create one
    if not c:
  	c = instansiate_camera()

    # Get timestamp
    timestamp = datetime.utcnow().strftime("%H%M%S")
    pic_name = "pic{}{}".format(timestamp, PNG_EXT)

    # Grab a frame
    frame = c.getImage()
    if write:
        frame.save(os.path.join(PIC_PATH, pic_name))
    return frame

def clear_picture_folder():
    print("Removing existing pictures from Pictures folder..")
    if os.path.exists(PIC_PATH):
        files = os.listdir(PIC_PATH)
        for f in files:
            file_path = os.path.join(PIC_PATH, f)
            os.remove(file_path)
    print("Pictures folder purged!")
    return
    

def crop_intersection(base_image, crop_dimensions, write=False, write_name = None):
    if isinstance(base_image, Image):
        #print("Cropping intersection from initial image..")
        intersection_image = base_image.crop(crop_dimensions)
        if write:  # Write out the intersection picture
            output_path = os.path.join(PIC_PATH, write_name)
            intersection_image.save(output_path)
            if os.path.exists(output_path):
                print("Intersection saved successfully!")    

#        print("Intersection cropped successfully!")    
        return intersection_image
        
    else:
        raise Exception("Unable to clip intersection from base image!")

def instansiate_camera():
    print("Creating connection to Camera..")
    c = Camera(-1)
    if isinstance(c, Camera):
        print("Connection to Camera successful!")
        return c

def instantiate_video_capture():
    vc = ''
    while not isinstance(vc, VideoCapture):
        try:
            print("Connecting to Video Camera..")
            vc = VideoCapture(-1)
        except Exception as err:
            print("Error instantiating VideoCapture object..")
            print("Retrying in 10 seconds..")
            time.sleep(10)
    return vc
def take_a_video(video_cam, duration, fps, output_path=PIC_PATH):
    # Takes a video for n seconds
    
    # Instantiate a videoCapture Object
    try:
        if video_cam is None:
            cap = cv2.VideoCapture(-1)
        else:
            cap = video_cam
    except Exception as err:
        raise err    

    # Get timestamps
    timestamp = datetime.utcnow().strftime("%H%M%S")

    # Establish output directory
    if os.path.exists(output_path):
        out_path = os.path.join(output_path, "video{}.avi".format(timestamp))
    else:
        raise Exception("Output path provided to take_a_video() does not exist!")

    # Directory for video to be written to
    try:
        fourcc = cv2.cv.CV_FOURCC(*'XVID')
        out = cv2.VideoWriter(out_path, fourcc, fps, FOUR_EIGHTY_RESOLUTION)
        #out = cv2.VideoWriter(out_path, fourcc, fps, SEVEN_TWENTY_RESOLUTION)
    except Exception as err:
        print("Error while initializing VideoWriter!")
        raise(err)

    # Start recording
    start_time = time.time()
    current_time = 0
    try:
        print("Recording for {} seconds..".format(duration))
        while current_time - start_time <= duration:        
            ret, frame = cap.read()

            current_time = time.time()
            time_delta = current_time - start_time
#            print("Recording for {} more second..".format(round(abs(time_delta - duration), 2)))

            if ret:
                out.write(frame)

                #if cv2.waitKey(1) & 0xFF == ord('q'):
                #    break
            else:
                print("Ret was FALSE!")
                break

    except exception as err:
        print("Something broke in the video while loop..")
        raise(err)

    finally:
        # Release everything
        #cap.release()
        #out.release()
        #cv2.destroyAllWindows()
        #del cap
        #del out
        print("Capture complete!")

    return 0


def crop_initial_video(initial_frame, crop_dimensions, output_name, output_path=PIC_PATH, write=False):
    # Crop focus AOI from an initial frame of video
    
    print("Cropping intersection from initial image..")
    crop = []
    focus_aoi = initial_frame[crop_dimensions[2]: crop_dimensions[3], crop_dimensions[0]:crop_dimensions[1]]
    if write is True:
        output_path = os.path.join(PIC_PATH, output_name)
        cv2.imwrite(output_path, focus_aoi)
        if os.path.exists(output_path):
            print("Intersection saved successfully!")    

#    print("Intersection cropped successfully!")    
    return focus_aoi
                


#def detect_change(initial_image, crop_dimensions,     


if __name__ == "__main__":
    raise Exception("This module is used for import only")
    sys.exit(1)
