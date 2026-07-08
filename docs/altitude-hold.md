# Altitude Hold

## Ziel

Stabile Höhenhaltung der Drohne im Innenbereich.

## Verwendete Komponenten

- ArduPilot
- LiDAR Sensor (MTF-01P)

## Durchführung

Der Flugmodus Altitude Hold wurde im Mission Planner aktiviert.

Mehrere Testflüge wurden durchgeführt.

Während der Tests wurde beobachtet, dass starke Vibrationen die Höhenregelung beeinflussen können.

## Beobachtungen

- Ruhiger Flug verbessert die Stabilität.
- Reduzierte Vibrationen führen zu besseren Ergebnissen.
- Die Drohne konnte ihre Höhe erfolgreich halten.

## Herausforderungen

- Das interne Barometer des Flight Controllers wurde zunächst für die Höhenmessung getestet.
- Aufgrund unzureichender Ergebnisse wurde zusätzlich ein LiDAR-Sensor integriert.
- Starke Vibrationen beeinflussten die Höhenregelung negativ.
- Mehrere Maßnahmen zur Vibrationsdämpfung wurden umgesetzt.

## Durchgeführte Anpassungen

- Kalibrierung des LiDAR-Sensors.
- Optimierung der Filterparameter zur Verbesserung der Stabilität.
- Verwendung von gedämpften Landefüßen zur Reduzierung von Vibrationen.
- Mehrere Testflüge zur Feinabstimmung der Höhenregelung.

## Erkenntnisse

- Ein ruhiger und vibrationsarmer Flug ist entscheidend für eine stabile Höhenhaltung.
- Die LiDAR-basierte Höhenmessung lieferte bessere Ergebnisse als das interne Barometer.

## Ergebnis

Altitude Hold funktioniert erfolgreich.
