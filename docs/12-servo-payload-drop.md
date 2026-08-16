# 12 – Servo Payload Drop

## Anschluss

| Kabel | Verbindung |
|---|---|
| Rot | 5V Flight Controller |
| Braun | GND Flight Controller |
| Orange | GPIO 18 / Pin 12 Raspberry Pi |

## Installation

```bash
sudo apt update
sudo apt install -y python3-gpiozero python3-rpi.gpio
```

## Test

```bash
python3 scripts/servo_test.py
```

## Zitterfrei

Der getestete Ablauf:
1. Position setzen.
2. 0,5 s warten.
3. `servo.detach()`.
4. warten.
5. nächste Position.
6. wieder `detach()`.

Damit wird das PWM-Signal während der Wartezeit abgeschaltet.

## Integration

Das KI-Skript ruft den Servo-Test als separates Programm auf:

```python
os.system("python3 scripts/servo_test.py")
```

Dadurch bleibt der Servo-Code unabhängig.
