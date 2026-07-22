# Delivery System

## Overview

Another part of the drone project is the development of a delivery mechanism.

The mechanical integration of this system requires a servo underneath the drone. This requirement influenced several other parts of the mechanical design, particularly the landing gear and the available space below the frame.

At the current stage of the project, work has been carried out on the mechanical preparation and integration required for the servo.

The complete autonomous delivery process is not documented as finished.

---

## Objectives

The work carried out in this part of the project focuses on:

- creating sufficient space for the servo,
- integrating the servo into the mechanical design,
- adapting the landing gear,
- maintaining sufficient ground clearance,
- considering vibration damping,
- preparing the mechanical structure for the delivery mechanism.

---

# 1. Servo Integration

A servo is required underneath the drone for the delivery mechanism.

During the mechanical development, it became clear that the available space underneath the original configuration was not sufficient.

This requirement directly influenced the design of the additional 3D-printed components.

---

# 2. Space Requirement

The servo required additional clearance between the drone frame and the ground.

The mechanical design therefore had to satisfy two requirements simultaneously:

1. provide sufficient space for the servo,
2. maintain stable support during landing.

This resulted in modifications to the landing gear.

---

# 3. First Landing-Gear Version

The first version of the landing feet was produced using 3D printing.

Damping material was added to reduce vibrations and landing impacts.

However, this version did not provide enough space underneath the drone for the servo.

The design therefore had to be modified.

---

# 4. Second Landing-Gear Version

A second version of the landing feet was developed.

The new feet were longer in order to create additional space underneath the drone.

The development can be summarized as:

```text
Landing Feet – Version 1
        ↓
Servo requires more clearance
        ↓
Landing Feet – Version 2
        ↓
Longer feet + vibration damping
```

The longer landing feet provided the additional clearance required for the servo.

---

# 5. Protective Cage Test

A larger cage was also tested during the mechanical development.

However, this configuration did not provide a suitable solution for the complete component arrangement.

One of the relevant limitations was the space still required for the servo.

For this reason, the tested larger cage was not retained in this form.

---

# 6. Vibration Damping

The landing-gear modifications were not only required for the servo.

Vibration damping was also an important consideration.

Damping material was therefore incorporated into both landing-gear versions.

This was particularly relevant because vibrations also influenced other components of the drone, including the LiDAR mounting.

The mechanical development of the delivery system was therefore connected to the general vibration-reduction work of the project.

---

# 7. Relation to the Frame Design

The delivery mechanism cannot be considered separately from the frame development.

The following components all require space on or underneath the drone:

- LiDAR,
- Raspberry Pi,
- camera,
- servo,
- additional mounting components.

As a result, several mechanical designs had to be tested and modified during the project.

The detailed mechanical development is documented in:

```text
frame-design.md
```

---

# 8. Work Performed So Far

The following work related to the delivery mechanism has been documented so far:

- Servo space requirement identified.
- Mechanical integration of the servo considered during frame development.
- First version of the landing feet produced.
- Vibration damping added to the first version.
- Insufficient servo clearance identified.
- Longer second version of the landing feet produced.
- Vibration damping retained in the second version.
- Larger cage tested.
- Cage configuration found unsuitable for the required component arrangement.
- Mechanical structure adapted to provide space for the servo.

---

# 9. Current Status

The drone has been mechanically adapted to provide the space required for the servo.

The landing gear was redesigned specifically because the initial version did not provide sufficient clearance.

The delivery system should therefore currently be considered a **mechanical integration task that is still part of the ongoing project development**.

Based on the currently available project documentation, the complete autonomous delivery sequence is not yet documented as implemented or successfully tested.

For this reason, this documentation does not claim that autonomous payload delivery has already been completed.

Further information will be added when additional servo-control or delivery tests are performed.
