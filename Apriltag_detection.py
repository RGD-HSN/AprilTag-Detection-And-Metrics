# Import the necessary packages
import apriltag
import cv2
import numpy as np  # Make sure to import NumPy
import time  # Import the time module

# Define the AprilTags detector options for tag16h5
options = apriltag.DetectorOptions(families="tag16h5")
detector = apriltag.Detector(options)

# Start capturing video from the camera
print("[INFO] starting video stream...")
cap = cv2.VideoCapture(0)  # 0 is typically the default camera

# Set camera resolution (optional)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1900)  # Set width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)  # Set height

# Loop to continuously capture frames
while True:
    # Read a frame from the camera
    start_time = time.time()

    ret, frame = cap.read()
    if not ret:
        print("[ERROR] failed to capture image")
        break

    # Convert the frame to grayscale and apply Gaussian blur
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply binary thresholding
    _, thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)

    # Detect AprilTags in the thresholded image
    print("[INFO] detecting AprilTags...")
    results = detector.detect(thresh)
    print("[INFO] {} total AprilTags detected".format(len(results)))

    # Loop over the detected AprilTags
    for result in results:
        # Extract the bounding box (x, y)-coordinates for the AprilTag
        (top_left, top_right, bottom_right, bottom_left) = result.corners
        top_left = (int(top_left[0]), int(top_left[1]))
        top_right = (int(top_right[0]), int(top_right[1]))
        bottom_right = (int(bottom_right[0]), int(bottom_right[1]))
        bottom_left = (int(bottom_left[0]), int(bottom_left[1]))

        # Calculate the center of the AprilTag
        center_x = int((top_left[0] + bottom_right[0]) / 2)
        center_y = int((top_left[1] + bottom_right[1]) / 2)
        center = (center_x, center_y)

        # Draw the bounding box of the AprilTag on the frame
        cv2.polylines(frame, [np.array([top_left, top_right, bottom_right, bottom_left], dtype=np.int32)],
                      isClosed=True, color=(0, 255, 0), thickness=2)

        # Draw the center of the AprilTag on the frame
        cv2.circle(frame, center, 5, (255, 0, 0), -1)  # Blue circle for the center

        # Display the center location on the frame
        cv2.putText(frame, f"Center: ({center_x}, {center_y})", (center_x + 10, center_y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Draw the tag ID on the frame
        cv2.putText(frame, str(result.tag_id), (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0, 255, 0), 2)

    # Display the output frame
    cv2.imshow("AprilTag Detection", frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cycle_time = time.time() - start_time
    print(f"[INFO] Cycle time: {cycle_time:.4f} seconds")
# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
