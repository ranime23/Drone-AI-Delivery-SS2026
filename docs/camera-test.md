# Raspberry Pi Camera Test

## Objective

The objective of this test was to verify that the Raspberry Pi camera can capture images, save them locally and make the generated files accessible through the local network.

This test represents a first technical step toward future camera-based image processing and object-recognition functions.

---

# 1. Hardware

- Raspberry Pi Zero 2 W
- Raspberry Pi AI Camera
- Camera connection cable
- Laptop for SSH access and test evaluation

---

# 2. Network Connection

The Raspberry Pi was accessed through the configured local network.

A connection between the laptop and Raspberry Pi was successfully established.

---

# 3. Camera Connection

The camera was connected to the Raspberry Pi using the corresponding ribbon cable.

The Raspberry Pi was then checked to verify that the camera could be used.

---

# 4. Test Image Capture

Several test images were captured.

The documented files include:

```text
test.jpg
test2.jpg
test3.jpg
test4.jpg
test5.jpg
```

The images were stored on the Raspberry Pi.

---

# 5. Image Verification

The captured images were opened and visually checked.

The camera successfully captured images of the environment and people present during the test.

This confirmed the basic image-capture functionality.

---

# 6. Local Network File Access

A local HTTP server was used to access the generated files.

The documented local address was:

```text
10.42.0.1:8000
```

A directory listing was displayed in the browser and the generated test images were visible.

This confirmed that the images could be accessed from the laptop through the local network.

---

# 7. Result

The basic camera test was successful.

The following functions were verified:

- camera connected to Raspberry Pi,
- image capture,
- local image storage,
- creation of multiple test images,
- image opening and visual inspection,
- access to files through the local network,
- communication between laptop and Raspberry Pi for file access.

---

# 8. Current Status

The basic camera functionality has been successfully tested.

However, this test does not demonstrate complete AI-based image processing or autonomous object recognition.

The result provides a technical basis for future computer-vision development.

---

# 9. Next Steps

- integrate the camera into the Raspberry Pi software,
- process images with OpenCV,
- test continuous image capture or video streaming,
- develop object detection,
- connect image-processing results to future autonomous drone functions.
