from gpiozero import Servo
from time import sleep

servo = Servo(
    18,
    min_pulse_width=0.5 / 1000,
    max_pulse_width=2.5 / 1000
)

try:
    print("--- 90-GRAD ABWURF TEST (ZITTERFREI) ---")

    print("Position: HALTEN")
    servo.value = 0.0
    sleep(0.5)
    servo.detach()
    sleep(2.5)

    print("Position: ABWURF")
    servo.value = 1.0
    sleep(0.5)
    servo.detach()
    sleep(1.5)

    print("Position: ZURÜCK")
    servo.value = 0.0
    sleep(0.5)
    servo.detach()
    sleep(1.5)

except KeyboardInterrupt:
    pass
finally:
    servo.detach()
    print("Fertig!")
