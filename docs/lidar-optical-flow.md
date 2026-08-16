# LiDAR und Optical Flow

## 1. Ziel

Verbesserung der Navigation und Flugstabilität im Innenbereich.

## 2. Sensor

Verwendet wurde der:

```text
MicroAir MTF-01P
```

## 3. LiDAR

Der LiDAR-Sensor wird für die Abstandsmessung zum Boden verwendet.

Hauptfunktion:
- Höhenmessung
- Unterstützung von Altitude Hold

Der Sensor wurde installiert, konfiguriert und kalibriert.

## 4. Optical Flow

Optical Flow erkennt Bewegungen der Drohne relativ zur Bodenfläche.

Hauptfunktion:
- Erkennung horizontaler Bewegungen
- Unterstützung von Position Hold

## 5. Kombination der Sensoren

Die Kombination aus LiDAR und Optical Flow ermöglicht eine GPS-unabhängige Flugregelung im Innenbereich.

```text
LiDAR
  |
  +--> Höhe
  |
  v
Altitude Hold

Optical Flow
  |
  +--> relative Bewegung
  |
  v
Position Hold
```

## 6. Tests

Es wurden mehrere Testflüge durchgeführt.

Die Ergebnisse zeigten, dass:
- reduzierte Vibrationen die Sensorik verbessern,
- LiDAR die Höhenregelung unterstützt,
- Optical Flow die Positionshaltung verbessert,
- die Kombination beider Sensoren GPS-unabhängige Navigation unterstützt.

## 7. Ergebnis

LiDAR und Optical Flow wurden erfolgreich in die Flugregelung integriert und getestet.
