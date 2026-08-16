# EXPERIMENTAL ONLY
# ArUco is computer vision, not neural AI.
# Test without propellers before any real autonomous-flight experiment.

import time
import cv2
import numpy as np
from gpiozero import Servo
from pymavlink import mavutil

master = mavutil.mavlink_connection("/dev/ttyAMA0", baud=57600)
master.wait_heartbeat()

servo = Servo(18)
servo.min()

FRAME_WIDTH = 640
FRAME_HEIGHT = 480
CENTER_X = FRAME_WIDTH // 2
CENTER_Y = FRAME_HEIGHT // 2
TARGET_ID = 0

def send_velocity(vx, vy, vz, yaw_rate=0.0):
    master.mav.set_position_target_local_ned_send(
        0,
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_FRAME_BODY_NED,
        0b011111000111,
        0, 0, 0,
        vx, vy, vz,
        0, 0, 0,
        0, yaw_rate
    )

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

if hasattr(cv2.aruco, "ArucoDetector"):
    detector = cv2.aruco.ArucoDetector(dictionary)
else:
    detector = None

cap = cv2.VideoCapture(0)

state = "SEARCH_PATTERN"
search_timer = time.time()
search_direction = 1

try:
    while True:

        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if detector is not None:
            corners, ids, _ = detector.detectMarkers(gray)
        else:
            corners, ids, _ = cv2.aruco.detectMarkers(gray, dictionary)

        if state == "SEARCH_PATTERN":

            vx = 0.3
            yaw = 0.1 * search_direction

            if time.time() - search_timer > 4:
                search_direction *= -1
                search_timer = time.time()

            send_velocity(vx, 0.0, 0.0, yaw)

            if ids is not None and TARGET_ID in ids.flatten():
                state = "CENTERING"

        elif state == "CENTERING":

            if ids is None or TARGET_ID not in ids.flatten():
                send_velocity(0, 0, 0, 0)
                state = "SEARCH_PATTERN"
                continue

            index = np.where(ids.flatten() == TARGET_ID)[0][0]
            marker = corners[index][0]

            marker_x = int(np.mean(marker[:, 0]))
            marker_y = int(np.mean(marker[:, 1]))

            err_x = marker_x - CENTER_X
            err_y = marker_y - CENTER_Y

            kP = 0.0015
            vy = np.clip(err_x * kP, -0.4, 0.4)
            vx = np.clip(-err_y * kP, -0.4, 0.4)

            send_velocity(vx, vy, 0.0, 0.0)

            if abs(err_x) < 20 and abs(err_y) < 20:

                send_velocity(0, 0, 0, 0)
                time.sleep(1)
                state = "DROP"

        elif state == "DROP":

            servo.max()
            time.sleep(2)
            servo.min()
            state = "FINISHED"

        elif state == "FINISHED":

            send_velocity(0, 0, 0, 0)
            break

finally:

    send_velocity(0, 0, 0, 0)
    servo.detach()
    cap.release()
    cv2.destroyAllWindows()
