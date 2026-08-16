import cv2
import os
from time import sleep

CONFIDENCE_THRESHOLD = 0.5
TARGET_CLASS = "bottle"

CLASSES = [
    "background", "aeroplane", "bicycle", "bird", "boat", "bottle",
    "bus", "car", "cat", "chair", "cow", "diningtable", "dog",
    "horse", "motorbike", "person", "pottedplant", "sheep", "sofa",
    "train", "tvmonitor"
]

MODEL_PROTOTXT = "MobileNetSSD_deploy.prototxt"
MODEL_WEIGHTS = "MobileNetSSD_deploy.caffemodel"

print("[INIT] Lade MobileNet-SSD...")
net = cv2.dnn.readNetFromCaffe(MODEL_PROTOTXT, MODEL_WEIGHTS)

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

if hasattr(cv2.aruco, "DetectorParameters_create"):
    parameters = cv2.aruco.DetectorParameters_create()
else:
    parameters = cv2.aruco.DetectorParameters()

gst_pipeline = (
    "libcamerasrc ! "
    "video/x-raw, width=640, height=480, framerate=30/1 ! "
    "videoconvert ! "
    "video/x-raw, format=BGR ! "
    "appsink drop=1"
)

cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)

if not cap.isOpened():
    raise RuntimeError("Kamera konnte nicht gestartet werden.")

for _ in range(30):
    cap.read()

state = "SEARCH_AI"

try:
    while True:
        success, frame = cap.read()
        if not success or frame is None:
            continue

        if state == "SEARCH_AI":

            blob = cv2.dnn.blobFromImage(
                cv2.resize(frame, (300, 300)),
                0.007843,
                (300, 300),
                127.5
            )

            net.setInput(blob)
            detections = net.forward()

            for i in range(detections.shape[2]):

                confidence = detections[0, 0, i, 2]

                if confidence > CONFIDENCE_THRESHOLD:

                    idx = int(detections[0, 0, i, 1])

                    if CLASSES[idx] == TARGET_CLASS:

                        print(
                            f"[KI] {TARGET_CLASS}: "
                            f"{confidence * 100:.1f}%"
                        )

                        state = "VERIFY_ARUCO"
                        break

        elif state == "VERIFY_ARUCO":

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if hasattr(cv2.aruco, "ArucoDetector"):
                detector = cv2.aruco.ArucoDetector(dictionary, parameters)
                corners, ids, _ = detector.detectMarkers(gray)
            else:
                corners, ids, _ = cv2.aruco.detectMarkers(
                    gray, dictionary, parameters=parameters
                )

            if ids is not None:

                print(f"[ARUCO] erkannt: {ids.flatten()}")
                state = "DROP"

            else:

                print("[ARUCO] Suche...")
                sleep(0.3)

        elif state == "DROP":

            print("[DROP] Starte Servo...")
            code = os.system("python3 scripts/servo_test.py")

            if code == 0:
                print("[DROP] erfolgreich ausgelöst.")
            else:
                print(f"[DROP] Fehlercode: {code}")

            state = "FINISHED"

        elif state == "FINISHED":

            print("=== MISSION ABGESCHLOSSEN ===")
            break

except KeyboardInterrupt:
    print("Abgebrochen.")

finally:
    cap.release()
