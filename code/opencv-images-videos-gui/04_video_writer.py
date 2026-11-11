"""
Video Writer: Saving video to files.

This script demonstrates:
- Capturing from webcam and saving to file
- Using VideoWriter with different codecs
- Setting frame rate and resolution
"""

import cv2


OUTPUT_FILE = 'output.mp4'
CODEC = 'MP4V'  # Common options: 'XVID' (.avi), 'MP4V' (.mp4), 'MJPG' (.avi)
FPS = 30
DURATION_SECONDS = 10


def record_video():
    """Record video from webcam and save to file."""
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Could not open camera")
        return

    # Get frame dimensions from camera
    width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(f"Recording at {width}x{height}, {FPS} fps")
    print(f"Output file: {OUTPUT_FILE}")
    print(f"Codec: {CODEC}")
    print(f"Duration: {DURATION_SECONDS} seconds")
    print()

    # Create VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*CODEC)
    writer = cv2.VideoWriter(OUTPUT_FILE, fourcc, FPS, (width, height))

    if not writer.isOpened():
        print("Error: Could not open VideoWriter")
        camera.release()
        return

    frames_to_record = FPS * DURATION_SECONDS
    frames_recorded = 0

    print("Recording... Press 'q' to stop early")

    while frames_recorded < frames_to_record:
        success, frame = camera.read()
        if not success:
            print("Failed to read frame")
            break

        writer.write(frame)
        frames_recorded += 1

        # Show preview
        cv2.imshow('Recording', frame)

        # Show progress
        if frames_recorded % FPS == 0:
            seconds_done = frames_recorded // FPS
            print(f"  {seconds_done}/{DURATION_SECONDS} seconds")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Recording stopped early")
            break

    # Clean up
    camera.release()
    writer.release()
    cv2.destroyAllWindows()

    print()
    print(f"Done! Recorded {frames_recorded} frames to '{OUTPUT_FILE}'")


if __name__ == '__main__':
    record_video()
