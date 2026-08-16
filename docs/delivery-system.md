# Payload Delivery System

## 1. Ziel

Die Drohne soll eine kleine Nutzlast transportieren und diese nach erfolgreicher Zielerkennung freigeben.

## 2. Servo

Verwendet wird:

```text
Miuzei Micro Servo 9g MS18
```

Der Servo besitzt drei Anschlüsse:

```text
Braun  -> GND
Rot    -> 5V
Orange -> PWM signal
```

Für einen direkten Flight-Controller-Anschluss kann ein PWM-Ausgang wie M5 verwendet werden, sofern dieser entsprechend konfiguriert ist.

Alternativ wurde für den Prototyp das Signal des Servos über GPIO 18 des Raspberry Pi getestet.

## 3. Raspberry-Pi-Anschluss

Beim getesteten Pi-Aufbau:

```text
Servo orange -> GPIO 18 / Pin 12
Servo brown  -> GND
Servo red    -> 5V
```

Für den Hybrid-Aufbau wurde empfohlen, die Stromversorgung des Servos vom Flight Controller zu beziehen und nur das Steuersignal über GPIO 18 zu führen.

## 4. Servo-Test

Der Servo wurde erfolgreich auf eine 90°-Position bewegt.

Eine wichtige Verbesserung war das Abschalten des PWM-Signals nach der Bewegung:

```python
servo.value = 1.0
sleep(0.5)
servo.detach()
```

Dadurch wird das Zittern während der Wartezeit reduziert.

## 5. Testlogik

```text
HALTEN
  |
  v
90° ABWURF
  |
  v
PWM detach
  |
  v
Nutzlast freigegeben
```

## 6. Automatische Missionslogik

Das geplante Gesamtsystem verwendet folgende Zustände:

```text
SEARCH_AI
    |
    | KI erkennt Ziel
    v
SEARCH_ARUCO
    |
    +---- Timeout ----> COOLDOWN -> AUTO
    |
    | ArUco gefunden
    v
DROP
    |
    v
RTL
    |
    v
FINISHED
```

## 7. Sicherheitslogik

Die KI-Erkennung allein soll nicht unmittelbar den Abwurf auslösen.

Stattdessen:
1. MobileNet-SSD erkennt die Zielklasse.
2. Die Drohne stoppt bzw. stabilisiert.
3. ArUco verifiziert das Ziel.
4. Erst danach wird der Servo ausgelöst.
5. Anschließend wird RTL aktiviert.

Diese zweistufige Erkennung reduziert das Risiko eines Abwurfs an einem falschen Ziel.

## 8. Status

Der Servo und die Abwurfbewegung wurden separat getestet.

Die vollständige integrierte Sequenz

```text
autonomer Flug
-> KI-Erkennung
-> ArUco-Verifizierung
-> Abwurf
-> RTL
```

soll nur nach einem erfolgreichen End-to-End-Flugtest als vollständig demonstriert dokumentiert werden.
