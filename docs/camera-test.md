# Camera and ArUco Test

## 1. Ziel

Test der Raspberry-Pi-Kamera für die spätere Objekterkennung und ArUco-Verifizierung.

## 2. Kamera

Die Raspberry Pi AI Camera wurde für die Bildverarbeitung verwendet.

Ein separater Testaufbau konnte die Kamera erfolgreich über `libcamerasrc` öffnen.

Beispiel:

```python
cap = cv2.VideoCapture(
    "libcamerasrc ! video/x-raw, width=640, height=480, framerate=30/1 ! videoconvert ! appsink",
    cv2.CAP_GSTREAMER
)
```

## 3. ArUco

Verwendet wird:

```text
DICT_4X4_50
```

Die Kamera wurde auf ArUco-Marker getestet.

Die Marker-Erkennung erfolgt mit OpenCV:

```python
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

corners, ids, rejected = cv2.aruco.detectMarkers(
    gray,
    dictionary,
    parameters=parameters
)
```

## 4. Kamerakalibrierung

Eine Kalibrierungsdatei kann verwendet werden:

```text
camera_calibration.npz
```

mit:

```text
camera_matrix
dist_coeffs
```

## 5. Hardware-ISP Initialisierung

Vor dem eigentlichen Test wurden mehrere Frames gelesen, um die Kamera zu initialisieren:

```python
for _ in range(60):
    cap.read()
```

## 6. Test

Bei erfolgreicher Erkennung wird die erkannte Marker-ID ausgegeben:

```text
Target Acquired. ID Array: [...]
```

## 7. MobileNet-SSD

Für die Objekterkennung ist ein vortrainiertes MobileNet-SSD vorgesehen.

Konfiguration:

```text
CONFIDENCE_THRESHOLD = 0.5
TARGET_CLASS = "bottle"
```

Das Modell besteht aus:

```text
MobileNetSSD_deploy.prototxt
MobileNetSSD_deploy.caffemodel
```

## 8. Architektur

```text
Camera
   |
   v
OpenCV
   |
   +--> MobileNet-SSD
   |       |
   |       +--> Target detected
   |
   +--> ArUco
           |
           +--> Target verified
```

## 9. Hinweis

Bei einem integrierten Skript trat ein Kamera-/GStreamer-Fehler auf:

```text
Failed to allocate required memory
unable to start pipeline
Kein Kamerabild!
```

Ein separater Kamera-Test mit `libcamerasrc` funktionierte jedoch und dient als Referenz für die korrekte Kameraanbindung.
