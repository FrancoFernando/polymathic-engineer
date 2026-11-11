"""
Video Capture: Reading video from files and cameras.

This script demonstrates:
- Reading frames from a video file
- Capturing frames from a webcam
- The frame-by-frame processing loop

Set USE_CAMERA to True to capture from webcam, False to read from file.
"""

import cv2


USE_CAMERA = True  # Set to False to read from a video file instead
VIDEO_FILE = 'input.avi'  # Change this to your video file path


def capture_from_camera():
    """Capture and display frames from the default webcam."""
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Could not open camera")
        return

    print("Camera opened successfully")
    print(f"Frame width: {camera.get(cv2.CAP_PROP_FRAME_WIDTH)}")
    print(f"Frame height: {camera.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
    print("Press 'q' to quit")
    print()

    while True:
        success, frame = camera.read()
        if not success:
            print("Failed to read frame")
            break

        cv2.imshow('Camera Feed', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()
    print("Camera released")


def capture_from_file(filepath):
    """Read and display frames from a video file."""
    video = cv2.VideoCapture(filepath)

    if not video.isOpened():
        print(f"Error: Could not open video file '{filepath}'")
        return

    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(f"Video opened: {filepath}")
    print(f"Resolution: {width}x{height}")
    print(f"FPS: {fps}")
    print(f"Total frames: {frame_count}")
    print("Press 'q' to quit")
    print()

    delay = int(1000 / fps) if fps > 0 else 33  # milliseconds between frames

    while True:
        success, frame = video.read()
        if not success:
            print("End of video")
            break

        cv2.imshow('Video Playback', frame)

        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    if USE_CAMERA:
        capture_from_camera()
    else:
        capture_from_file(VIDEO_FILE)
