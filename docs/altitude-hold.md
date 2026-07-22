# Altitude Hold

## Overview

Altitude Hold was one of the first autonomous flight modes implemented during the project.

The objective was to enable the drone to maintain a constant altitude without continuous pilot throttle corrections. Achieving a stable altitude was considered an important milestone before implementing Position Hold and autonomous navigation.

Since the project mainly focuses on indoor flight, reliable altitude estimation was required without depending on GPS.

---

# Objective

The objectives of this work package were:

- Maintain a constant flight altitude
- Improve hover stability
- Reduce manual pilot corrections
- Integrate a LiDAR sensor for altitude measurement
- Prepare the system for Position Hold

---

# Hardware

| Component | Purpose |
|-----------|----------|
| Flywoo GOKU GN745 | Flight Controller |
| MicroAir MTF-01P | LiDAR distance sensor |
| ELRS Receiver | Manual control during testing |

---

# Initial Approach

The first implementation relied on the internal barometer of the Flight Controller.

Several flight tests were carried out to evaluate whether the internal pressure sensor could provide sufficient altitude estimation for indoor flights.

However, the obtained results were not satisfactory.

The altitude estimation fluctuated significantly, leading to unstable hovering.

---

# LiDAR Integration

To improve altitude estimation, a MicroAir MTF-01P LiDAR sensor was installed.

The sensor was mounted underneath the drone and carefully aligned to measure the distance between the aircraft and the ground.

After installation, the sensor was calibrated using Mission Planner.

The LiDAR became the primary altitude source for low-altitude indoor flights.

---

# LiDAR Configuration

The following parameters were configured inside Mission Planner.

| Parameter | Value |
|-----------|-------|
| RNGFND1_MAX_CM | 700 |
| RNGFND1_MIN_CM | 20 |
| RNGFND1_GNDCLEAR | 10 |
| RNGFND1_ORIENT | Downward |
| RNGFND1_POS_X | 0.05 |
| RNGFND1_POS_Z | 0.01 |

These parameters define the measurement range, mounting position and orientation of the sensor.

---

# Flight Testing

Several indoor flight tests were performed.

During every test the following aspects were evaluated:

- Hover stability
- Altitude accuracy
- Sensor response
- Influence of vibrations
- Repeatability of the altitude controller

Whenever unstable behaviour was observed, the drone landed and new adjustments were made before repeating the test.

---

# Vibration Analysis

One of the biggest challenges during Altitude Hold was vibration.

Strong vibrations affected both the Flight Controller sensors and the LiDAR measurements.

Several mechanical improvements were introduced:

- Additional vibration damping
- Improved landing feet
- Foam damping material
- Better cable routing
- Secure mounting of the LiDAR sensor

These modifications significantly improved measurement stability.

---

# Challenges

Several difficulties occurred during development.

## Internal Barometer

The internal Flight Controller barometer did not provide reliable altitude estimation during indoor flights.

Therefore, another sensor solution became necessary.

---

## Sensor Calibration

The LiDAR sensor required several calibration procedures before stable measurements were obtained.

The sensor position also had to be adjusted after mechanical modifications.

---

## Flight Stability

Altitude Hold depends heavily on a stable aircraft.

Large oscillations negatively influenced the altitude controller.

For this reason, flight controller tuning and vibration reduction were completed before extensive Altitude Hold testing.

---

# Results

The following milestones were achieved successfully:

- Successful LiDAR installation
- Successful sensor calibration
- Stable altitude estimation
- Reliable indoor hovering
- Reduced vibration influence
- Successful Altitude Hold implementation

The drone was able to maintain its altitude significantly better than during the initial barometer-based tests.

---

# Lessons Learned

During development several important observations were made.

- Indoor altitude estimation cannot rely solely on the internal barometer.
- LiDAR provides significantly more accurate altitude information at low heights.
- Flight stability and vibration reduction are essential before enabling autonomous flight modes.
- Mechanical improvements directly influence sensor performance.

---

# Next Steps

After successfully implementing Altitude Hold, the next development phase focused on:

- Position Hold
- Optical Flow integration
- Indoor navigation
- Autonomous object delivery
