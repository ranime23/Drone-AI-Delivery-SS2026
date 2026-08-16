# Delivery System

## Overview

The delivery system is intended to allow the drone to transport and release a payload.

The mechanical integration requires a servo underneath the drone.

This requirement influenced the landing gear and the available space below the frame.

---

# 1. Objectives

The documented work focuses on:

- creating sufficient space for the servo,
- integrating the servo mechanically,
- adapting the landing gear,
- maintaining ground clearance,
- reducing vibration,
- preparing the mechanical structure for payload release.

---

# 2. Servo Requirement

A servo is required underneath the drone for the delivery mechanism.

During the mechanical development, the available space was found to be insufficient in the original configuration.

This requirement directly influenced the 3D-printed components.

---

# 3. Landing Gear Version 1

The first landing-gear version was 3D printed and equipped with damping material.

However, it did not provide enough clearance for the servo.

A second version was therefore developed.

---

# 4. Landing Gear Version 2

The second version used longer landing feet.

The objective was to create additional space underneath the drone for the servo.

Damping material was retained.

```text
Version 1
    ↓
Servo requires more clearance
    ↓
Version 2
Longer landing feet + damping
```

---

# 5. Larger Cage

A larger cage was tested during mechanical development.

The configuration was not suitable for the required component arrangement, particularly because additional space was still required for the servo.

The tested cage was therefore not retained in that form.

---

# 6. Relation to Frame Design

The delivery mechanism is directly connected to the mechanical frame design.

The following components compete for available space:

- LiDAR,
- Raspberry Pi,
- camera,
- servo,
- additional mounting components.

The detailed mechanical work is documented in:

```text
frame-design.md
```

---

# 7. Current Status

The mechanical preparation for the servo has been performed.

However, the current documentation does **not** provide evidence that the complete autonomous payload-release sequence has been successfully implemented and tested.

Therefore, the delivery system should currently be documented as an ongoing integration task.

---

# 8. Next Steps

- final servo integration,
- servo-control test,
- mechanical release test,
- payload-release test,
- Raspberry-Pi control integration,
- autonomous release logic,
- final flight test with payload.
