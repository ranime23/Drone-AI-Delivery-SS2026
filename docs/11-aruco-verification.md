# 11 – ArUco Verification

## Dictionary

```python
cv2.aruco.DICT_4X4_50
```

Target ID im Prototyp:

```text
0
```

## API

Je nach OpenCV-Version:

```python
if hasattr(cv2.aruco, "ArucoDetector"):
    detector = cv2.aruco.ArucoDetector(dictionary, parameters)
    corners, ids, _ = detector.detectMarkers(gray)
else:
    corners, ids, _ = cv2.aruco.detectMarkers(
        gray, dictionary, parameters=parameters
    )
```

## Logik

```text
SEARCH_AI
 ↓
MobileNet findet bottle
 ↓
VERIFY_ARUCO
 ↓
Marker gefunden?
 ├─ nein → weiter prüfen
 └─ ja → DROP
```

## Test

Vor dem Flug:
1. Marker drucken.
2. Kamera starten.
3. ID 0 zeigen.
4. Erkennung aus mehreren Abständen testen.
5. Erst danach mit MobileNet kombinieren.

ArUco selbst ist keine neuronale KI.
