# Raspberry Pi Camera Test

## Ziel

Ziel dieses Tests war es, die am Raspberry Pi angeschlossene Kamera in Betrieb zu nehmen und zu überprüfen, ob Bilder erfolgreich aufgenommen, gespeichert und über die lokale Netzwerkverbindung abgerufen werden können.

Dieser Test stellt einen ersten Schritt für die spätere kamerabasierte Verarbeitung und die autonome Objekterkennung dar.

## Verwendete Hardware

- Raspberry Pi
- Raspberry Pi Camera
- Verbindungskabel der Kamera
- Laptop für SSH-Zugriff und Testauswertung

## Netzwerkverbindung

Der Raspberry Pi wurde über das bereits konfigurierte lokale Netzwerk erreicht.

Für den Zugriff wurde die lokale Netzwerkverbindung des Raspberry Pi verwendet.

Die Kommunikation zwischen Laptop und Raspberry Pi konnte erfolgreich hergestellt werden.

## Durchführung

### 1. Anschluss der Kamera

Die Raspberry-Pi-Kamera wurde über das entsprechende Flachbandkabel mit dem Raspberry Pi verbunden.

Anschließend wurde überprüft, ob der Raspberry Pi die Kamera verwenden kann.

### 2. Durchführung von Testaufnahmen

Mit der angeschlossenen Kamera wurden mehrere Testbilder aufgenommen.

Dabei wurden unter anderem folgende Dateien erzeugt:

- test.jpg
- test2.jpg
- test3.jpg
- test4.jpg
- test5.jpg

Die Dateien wurden auf dem Raspberry Pi gespeichert.

### 3. Überprüfung der aufgenommenen Bilder

Die erzeugten Bilder wurden anschließend geöffnet und visuell überprüft.

Die Kamera konnte ein Bild der Umgebung bzw. der anwesenden Personen erfolgreich aufnehmen.

Damit wurde bestätigt, dass die grundlegende Bildaufnahme funktioniert.

### 4. Zugriff über das lokale Netzwerk

Für den Zugriff auf die erzeugten Dateien wurde ein lokaler HTTP-Zugriff verwendet.

Die Dateien des Raspberry Pi konnten über folgende lokale Adresse aufgerufen werden:

`10.42.0.1:8000`

Im Browser wurde ein Directory Listing angezeigt, in dem unter anderem die erzeugten Testbilder sichtbar waren.

Dadurch konnte überprüft werden, dass die aufgenommenen Bilder nicht nur lokal auf dem Raspberry Pi gespeichert werden, sondern auch über die bestehende Netzwerkverbindung vom Laptop aus erreichbar sind.

## Ergebnis

Der Kameratest war erfolgreich.

Folgende Funktionen konnten erfolgreich überprüft werden:

- Kamera ist mit dem Raspberry Pi verbunden.
- Bildaufnahme funktioniert.
- Testbilder können gespeichert werden.
- Mehrere Testbilder wurden erfolgreich erzeugt.
- Die aufgenommenen Bilder können geöffnet und überprüft werden.
- Zugriff auf die Dateien über das lokale Netzwerk funktioniert.
- Die Kommunikation zwischen Laptop und Raspberry Pi für den Dateizugriff funktioniert.

Damit ist die grundlegende Kamera-Funktionalität erfolgreich getestet.

## Aktueller Stand

Die grundlegende Kamerafunktion wurde erfolgreich getestet.

Eine vollständige KI-basierte Bildverarbeitung oder autonome Objekterkennung wurde in diesem Test noch nicht nachgewiesen.

Der erfolgreiche Kameratest bildet jedoch die technische Grundlage für die weitere Integration der Bildverarbeitung.

## Nächste Schritte

- Integration der Kamera in die weitere Raspberry-Pi-Software
- Verarbeitung der aufgenommenen Bilder mit OpenCV
- Test einer kontinuierlichen Bildaufnahme bzw. eines Videostreams
- Integration der kamerabasierten Objekterkennung
- Verbindung der Bildverarbeitung mit der späteren autonomen Drohnensteuerung
