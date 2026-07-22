# Altitude Hold

## Overview

One of the next steps after the initial ArduPilot configuration was the implementation and testing of **Altitude Hold (AltHold)**.

The objective was to enable the drone to maintain its flight altitude with reduced manual throttle correction.

During the development process, different altitude measurement approaches were tested. The internal barometer of the flight controller was tested first. Since this did not provide satisfactory results for the intended use, a LiDAR sensor was installed and calibrated.

Altitude Hold is currently part of the ongoing flight testing and optimisation process.

---

## Objective

The work carried out in this part of the project focused on:

- testing Altitude Hold with ArduPilot,
- evaluating the internal barometer,
- installing the LiDAR sensor,
- configuring the LiDAR in Mission Planner,
- calibrating the sensor,
- reducing vibration effects,
- performing flight tests,
- improving the stability of the drone before further Position Hold tests.

---

## Initial Test with the Internal Barometer

The internal barometer of the flight controller was initially tested as an altitude source for Altitude Hold.

During the tests, the barometer did not provide satisfactory results for the intended AltHold operation.

For this reason, the project continued with an external LiDAR sensor to obtain a direct distance measurement between the drone and the ground.

---

## LiDAR Installation

The LiDAR sensor was mounted underneath the drone.

After mounting, the sensor was connected to the flight controller and configured in Mission Planner.

The sensor was then calibrated and tested.

The mechanical mounting of the LiDAR also became an important issue during the project because vibrations affected the installation. Additional damping and modifications to the landing gear were therefore introduced.

---

## LiDAR Configuration in Mission Planner

The Range Finder parameters were configured in Mission Planner.

The current configuration contains the following values:

| Parameter | Value | Function |
|-----------|------:|----------|
| `RNGFND1_MAX_CM` | 700 | Maximum measurement distance |
| `RNGFND1_MIN_CM` | 20 | Minimum measurement distance |
| `RNGFND1_GNDCLEAR` | 10 | Ground clearance |
| `RNGFND1_ORIENT` | 25 | Sensor orientation |
| `RNGFND1_POS_X` | 0.05 | Sensor position on X-axis |
| `RNGFND1_POS_Z` | 0.01 | Sensor position on Z-axis |
| `EK3_RNG_USE_HGT` | -1 | EKF rangefinder height configuration |

These values are part of the current drone configuration exported from Mission Planner.

---

## Measurement Range

The configured measurement range is:

- Minimum distance: **20 cm**
- Maximum distance: **700 cm**

This range defines the distance interval in which the LiDAR is configured to provide altitude measurements.

The ground clearance was configured as:

```text
RNGFND1_GNDCLEAR = 10
```

---

## Sensor Position

The physical position of the LiDAR relative to the flight controller was also entered into the ArduPilot configuration.

```text
RNGFND1_POS_X = 0.05
RNGFND1_POS_Z = 0.01
```

These parameters describe the sensor offset relative to the reference position of the flight controller.

---

## Sensor Orientation

The LiDAR is installed to measure the distance between the drone and the ground.

The corresponding orientation parameter in the current configuration is:

```text
RNGFND1_ORIENT = 25
```

This configuration was entered in Mission Planner as part of the Range Finder setup.

---

## Calibration and Testing

After installing the LiDAR, several calibration and test steps were necessary.

The work carried out included:

1. Mounting the LiDAR on the drone.
2. Connecting the sensor to the flight controller.
3. Configuring the Range Finder parameters in Mission Planner.
4. Calibrating the sensor.
5. Checking the distance measurements.
6. Performing flight tests.
7. Observing the behaviour of the drone in AltHold.
8. Investigating vibration problems.
9. Modifying the mechanical damping where necessary.

The calibration process required several adjustments during the project.

---

## Vibration Problems

Vibration was an important problem during the Altitude Hold development.

The drone had to remain sufficiently stable for the altitude measurement and AltHold tests.

The project group therefore worked on mechanical vibration reduction.

One problem was that the LiDAR mounting could be affected by the vibrations of the drone.

To improve this situation, damping material was introduced into the landing gear design.

---

## Landing Gear and Vibration Damping

The first version of the 3D-printed landing feet was equipped with damping material made from foam/pool-noodle material.

Later, longer landing feet were required because additional space was needed underneath the drone for the servo.

The second version also included vibration damping.

This was important not only for landing but also because excessive vibrations could affect the LiDAR mounting.

Therefore, the mechanical frame development and the Altitude Hold tests were directly connected.

---

## Flight Stability

Before Altitude Hold and later Position Hold could be tested reliably, the drone needed to fly as calmly as possible.

For this reason, the work on Altitude Hold was performed together with the ongoing ArduPilot tuning.

The following aspects were therefore relevant:

- PID adjustments,
- gyro filtering,
- accelerometer filtering,
- Dynamic Harmonic Notch filtering,
- mechanical vibration damping,
- LiDAR calibration.

The corresponding flight-controller parameters are documented separately in `autopilot.md`.

---

## Tests Performed So Far

The following work has been performed so far:

- Internal barometer tested for AltHold.
- Barometer results were not satisfactory for the intended operation.
- LiDAR mounted on the drone.
- LiDAR calibrated.
- Range Finder parameters configured in Mission Planner.
- LiDAR distance range configured.
- Sensor position configured.
- Sensor orientation configured.
- Multiple calibration steps performed.
- Flight behaviour observed during tests.
- Vibration problems investigated.
- Mechanical damping added to the landing gear.

---

## Current Status

The LiDAR has been installed and calibrated, and the required Range Finder configuration has been entered in Mission Planner.

The internal barometer was tested but did not provide satisfactory results for the intended AltHold operation.

Flight stability, vibration reduction and Altitude Hold behaviour continue to be evaluated during the current project development.

The work on Altitude Hold is therefore **not considered completely finished yet**. It remains connected to the ongoing flight tuning and sensor testing.

---

## Relation to Position Hold

Altitude stabilization is also important for the next development step, Position Hold.

The project group therefore first focused on obtaining a calm and stable flight behaviour before continuing with Position Hold testing.

The Position Hold development is documented separately in:

```text
position-hold.md
```
