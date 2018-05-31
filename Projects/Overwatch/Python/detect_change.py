import os
import cv2
import time
import sys
from datetime import datetime

class detect_change(object):
    """
    By default captures video in 720p    
    """

    # Misc Constants
    SEVEN_TWENTY_RESOLUTION = (1280, 720)
    FOUR_EIGHTY_RESOLUTION = (640, 480)

    def __init__(self, resolution=SEVEN_TWENTY_RESOLUTION, focus_areas=[], trigger_email=False):
        print("Starting detect_change..")
        self.resolution = resolution
        self.focus_areas = focus_areas
        self.cap = self._set_capture(self.resolution)
        self.output_path = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, "Output"))
        self.trigger_email = trigger_email

        # Initial Frame variables
        self.initial_pic_path = os.path.join(self.output_path, 'initial.png')
        self.initial_frame = self._reset_initial_frame()
        self.initial_frame_mean = self.initial_frame.mean()

        # Timers
        self.start_time = time.time()
        self.start_timestamp = datetime.utcnow().strftime("%y/%m/%d %H:%M:%S")
        self.end_timestamp = None

    def __enter__(self):
        if sys.platform == "win32":
            self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            self.video_ext = ".mp4"
            return self
        else:
            print("WARNING - Maybe be unstable. This module has not yet been tested non-Windows platforms")
            self.fourcc = cv2.cv.CV_FOURCC(*'XVID')
            self.video_ext = ".avi"
            return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing Camera..")
        self.cap.release()

        print("Motion Detection ran from:\n{} -> {}".format(self.start_timestamp, self.end_timestamp))
        return

    def _calibrate_frames(self, camera=None, frames=8):
        """
        Default skips 8 frames
        """
        if not camera:
            camera = self.cap

        for i in range(frames):
            ret, img = camera.read()
            pass
        return

    def _set_capture(self, resolution):
        v = cv2.VideoCapture(0)
        # Set resolution
        v.set(3, resolution[0])
        v.set(4, resolution[1])

        # Initial Steps #

        # Ramp-up Camera for 30 frames
        print("Ramping up camera..")
        self._calibrate_frames(v, frames=30)

        if v.isOpened():
            return v
        else:
            raise IOError("Error setting up camera!")

    def _get_a_frame(self):
        return self.cap.read()

    def _reset_initial_frame(self):
        # Calibrate camera for a few frames
        self._calibrate_frames()

        ret, frame = self._get_a_frame()
        cv2.imwrite(self.initial_pic_path, frame)

        # Calibrate camera for a few frames
        self._calibrate_frames()
        
        # Calculate the mean for the new Initial Image
        self.initial_frame = frame
        self.initial_frame_mean = self.initial_frame.mean()

        return frame

    def clear_picture_folder(self):
        print("Removing existing pictures from Pictures folder..")
        if os.path.exists(self.output_path):
            files = os.listdir(self.output_path)
            for f in files:
                file_path = os.path.join(self.output_path, f)
                ext = os.path.splitext(file_path)[1]
                if ext in [".png", ".avi", ".mp4"]:
                    os.remove(file_path)
        print("Pictures folder purged!")
        return

    def _get_frames(self, duration=10):
        """
        Defaults for 10 seconds
        """
        # Stuff
        current_time = 0

        # Iterate for specified duration
        print("Grabbing frames for {} seconds..".format(duration))
        last_reset_minute = None
        while current_time - self.start_time <= duration:

            # Set current time
            current_time = time.time()
            time_stamp = datetime.utcnow()

            # Get current frame
            ret, frame = self.cap.read()
            d = self._get_frame_diff(frame)

            # TODO - Get in-line printing working for difference.
            print("\r{}".format(d), end='')
            time.sleep(0.2)

            if abs(d) >= 2:
                print("\nSignificant change detected - {}!".format(round(d, 2)))
                #cv2.imwrite(os.path.join(self.output_path, "{}.png".format(time_stamp)), frame)
                #break

                print("Writing video..")
                self._write_video()
                current_time = time.time()
                print("Resetting initial frame")
                self._reset_initial_frame()
                time.sleep(0.3)

                print("Back to grabbing frames for {} seconds".format(round(duration - (current_time - self.start_time)), 2))

            # Reset the initial image every 60 seconds
            # TODO Randomize the second at which it resets each minute
            if time_stamp.minute != last_reset_minute and -0.6 <= d <= 0.6:
                #print("Resetting Initial Frame..")
                self._reset_initial_frame()
                last_reset_minute = time_stamp.minute
        self.end_timestamp = datetime.utcnow().strftime("%y/%m/%d %H:%M:%S")



    # TODO - Start using this
    def _add_text_to_frame(self, frame, string):

        # Text overlay
        font = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (10, 700)
        fontScale = 1
        fontColor = (255, 255, 255)
        lineType = 2

        return cv2.putText(frame, str(round(self._get_frame_diff(frame), 2)),
                           bottomLeftCornerOfText,
                           font,
                           fontScale,
                           fontColor,
                           lineType)


    def _get_frame_diff(self, frame):
        if self.initial_frame_mean:
            m = frame.mean()
            return self.initial_frame_mean - m

    def _write_video(self, duration=10):

        # Start recording
        time_stamp = datetime.utcnow().strftime("%y%m%d_%H%M%S")
        start_time = time.time()
        current_time = 0

        # Video Writing Object
        vo = cv2.VideoWriter(os.path.join(self.output_path, "{}{}".format(time_stamp, self.video_ext)), self.fourcc, 15.0,
                             self.SEVEN_TWENTY_RESOLUTION)

        # Text overlay
        font = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (10, 700)
        fontScale = 1
        fontColor = (255, 255, 255)
        lineType = 2

        while current_time - start_time <= duration:
            current_time = time.time()
            ret, frame = self.cap.read()
            if ret:
                cv2.putText(frame, str(round(self._get_frame_diff(frame), 2)),
                            bottomLeftCornerOfText,
                            font,
                            fontScale,
                            fontColor,
                            lineType)
                vo.write(frame)

        return



if __name__ == "__main__":
    print("Starting..")
    with detect_change() as a:
        a.clear_picture_folder()
        a._reset_initial_frame()
        a._get_frames(120)

    print("Complete!")
