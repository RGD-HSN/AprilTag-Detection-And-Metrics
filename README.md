# AprilTag Detection

## Overview
This project demonstrates real-time **AprilTag detection** using Python and OpenCV. AprilTags are 2D barcodes designed for reliable detection in robotics and computer vision applications. In this project, I experimented with **detection metrics**, camera processing, and visualization techniques to track the tags and analyze detection performance.

The system captures video from a webcam, detects AprilTags in each frame, and visualizes the results with bounding boxes, centers, and tag IDs. Additionally, cycle time for each frame is measured to evaluate real-time performance.

---

## Features
- Real-time detection of AprilTags using the `apriltag` Python library.
- Supports `tag16h5` family of AprilTags.
- Bounding boxes drawn around each detected tag.
- Centers of tags visualized with colored markers.
- Tag IDs displayed on frames.
- Optional Gaussian blur and thresholding for improved detection.
- Cycle time measurement for performance evaluation.

---

## Dependencies
The project uses the following Python libraries:
- `opencv-python`
- `numpy`
- `apriltag`
- `time` (built-in)
- `argparse` (optional, for parameterized scripts)

Install dependencies using pip:
```bash
pip install opencv-python numpy apriltag


