# Frame Design and Mechanical Modifications

## Overview

During the project, several mechanical modifications were made to the drone.

The original frame did not provide sufficient space for all additional components required during the development. In particular, space was needed for the LiDAR, Raspberry Pi, camera and servo.

For this reason, several custom 3D-printed components were designed, manufactured and tested.

The mechanical design was developed iteratively. Some components were kept, while others had to be modified or replaced after testing.

---

## Objectives

The mechanical work carried out so far focused on:

- creating mounting possibilities for additional components,
- creating space underneath the drone for the servo,
- mounting the Raspberry Pi,
- mounting and protecting the camera,
- improving the landing gear,
- reducing vibrations,
- improving the mechanical stability of the LiDAR mounting.

---

# 1. 3D-Printed Components

Several custom components were produced using 3D printing.

The documented components include:

- additional frame components,
- Raspberry Pi mounting plate,
- landing feet – Version 1,
- landing feet – Version 2,
- larger protective cage prototype,
- camera case.

The design changed several times during the project because new mechanical requirements appeared during integration and flight testing.

---

# 2. Larger Cage Prototype

A larger cage was tested during the mechanical development.

The intention was to provide more space and protection for the additional components.

However, this version was not suitable for the final configuration.

One important problem was the available space underneath the drone.

Additional space was required for the servo, and the larger cage configuration did not provide a suitable solution for the complete hardware arrangement.

Therefore, this design was not continued in its tested form.

---

# 3. Raspberry Pi Mount

A dedicated plate was designed for mounting the Raspberry Pi.

This component is referred to in the project documentation as the **Pi-Mount**.

The mounting plate was necessary because the Raspberry Pi was not part of the original FPV drone configuration and therefore required an additional mounting solution.

The Pi-Mount represents one of the custom mechanical components developed specifically for the project.

---

# 4. Landing Feet – Version 1

The first version of the landing feet was manufactured using 3D printing.

In addition to providing support during landing, damping material was added to the feet.

Material from a foam/pool noodle was used for this purpose.

The objective was to reduce the transmission of vibrations and impacts to the drone.

The first version demonstrated the need for mechanical damping, but another problem appeared later: more space was required underneath the drone for the servo.

This resulted in the development of a second version.

---

# 5. Landing Feet – Version 2

The second version of the landing feet was made longer than the first version.

The main reason for this modification was to create sufficient space underneath the drone for the servo.

The development therefore changed from:

```text
Version 1
3D-printed landing feet
        +
damping material

        ↓

Additional space required for servo

        ↓

Version 2
longer 3D-printed landing feet
        +
damping material
```

Vibration damping was retained in the second version.

This was particularly important because vibration problems also affected the LiDAR mounting.

---

# 6. Vibration Damping

Vibration became an important mechanical problem during the project.

The LiDAR was mounted on the drone and calibrated, but the mechanical attachment had to remain stable during flight.

According to the project development log, without sufficient damping, vibrations could affect the LiDAR attachment.

For this reason, damping material was incorporated into the landing gear.

The mechanical modifications therefore supported the sensor and flight-stability work being carried out in parallel.

---

# 7. Relation to LiDAR Integration

The mechanical frame development and LiDAR integration were directly connected.

The LiDAR had to be:

- securely mounted,
- correctly positioned,
- protected against excessive movement,
- sufficiently isolated from vibrations.

For this reason, the landing gear and damping solution were not only developed for landing.

They also contributed to maintaining the mechanical stability required for the LiDAR.

The LiDAR configuration itself is documented in:

```text
lidar-optical-flow.md
```

and:

```text
altitude-hold.md
```

---

# 8. Servo Clearance

The integration of the servo created an additional mechanical requirement.

The first landing-gear configuration did not provide sufficient clearance underneath the drone.

Therefore, longer landing feet were required.

This modification created additional space for the servo and influenced the second version of the landing gear.

The servo-related mechanical work is documented separately in:

```text
delivery-system.md
```

---

# 9. Camera Case

A custom case was also produced for the camera.

The camera case was 3D printed and subsequently attached to the drone.

This provided a dedicated mounting solution for the camera instead of relying on the original frame configuration.

---

# 10. Iterative Development

The mechanical development was not completed in a single design step.

Instead, the parts were progressively adapted to problems discovered during integration.

The documented development process can be summarized as follows:

```text
Additional components required
            ↓
Custom 3D-printed parts
            ↓
Larger cage tested
            ↓
Space problem for servo
            ↓
Landing feet Version 1
            ↓
Need for additional clearance
            ↓
Landing feet Version 2
            ↓
Vibration damping retained
            ↓
Improved space for servo and LiDAR mounting
```

This iterative approach allowed the mechanical design to be adapted to the actual requirements discovered during the project.

---

# 11. Work Performed So Far

The following mechanical work has been carried out:

- 3D-printed components manufactured and installed.
- Larger cage tested.
- Larger cage configuration found unsuitable for the required servo space.
- Raspberry Pi mounting plate designed.
- First version of the landing feet printed.
- Damping material added to Version 1.
- Need for additional servo clearance identified.
- Longer landing feet developed as Version 2.
- Damping material also added to Version 2.
- Mechanical vibration problems investigated.
- LiDAR mounting considered during vibration-reduction work.
- Camera case printed.
- Camera case attached to the drone.

---

# 12. Current Status

Several mechanical modifications have already been implemented on the drone.

The development has progressed through multiple design iterations rather than one final frame design.

The current mechanical work includes the mounting solutions and modifications required for the additional project hardware, especially the Raspberry Pi, camera, LiDAR and servo.

Further mechanical changes can still be made as the integration and flight tests continue.

For this reason, the frame design is documented as an **ongoing iterative development process** rather than as a completely finished design.
