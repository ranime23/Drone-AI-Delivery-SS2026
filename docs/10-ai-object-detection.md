# 10 – KI Object Detection

## MobileNet-SSD

Die dokumentierte KI-Komponente ist ein vortrainiertes MobileNet-SSD über OpenCV DNN.

```python
net = cv2.dnn.readNetFromCaffe(
    "MobileNetSSD_deploy.prototxt",
    "MobileNetSSD_deploy.caffemodel"
)
```

Konfiguration:

```python
CONFIDENCE_THRESHOLD = 0.5
TARGET_CLASS = "bottle"
```

## Keine eigene Trainingsphase

Für den dokumentierten Prototyp wird ein vortrainiertes Modell verwendet.

Ein eigenes Training wäre nur notwendig, wenn eine projektspezifische Klasse benötigt wird, die nicht vom verwendeten Modell unterstützt wird.

## KI vs. ArUco

```text
MobileNet-SSD
= neuronale KI / Object Detection

ArUco
= deterministische Computer Vision / Marker Detection
```

Zusammen:

```text
Kamera
 ↓
MobileNet-SSD
 ↓
Zielobjekt erkannt
 ↓
ArUco
 ↓
Ziel verifiziert
 ↓
Servo
```

## Wichtig

Der aktuelle `ki_autonom_abwurf.py`-Prototyp implementiert Vision + Verifizierung + Servo. Er enthält nicht automatisch einen vollständig validierten autonomen Rasterflug. Die experimentelle MAVLink-Flugsteuerung ist separat dokumentiert.
