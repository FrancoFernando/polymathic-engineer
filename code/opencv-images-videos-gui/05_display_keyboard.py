"""
Display and Keyboard Input: Showing images and handling key presses.

This script demonstrates:
- Displaying images with imshow
- Using waitKey for keyboard input
- Responding to different key presses
"""

import cv2
import numpy as np


def display_static_image():
    """Display a static image and wait for a key press."""
    # Create a sample image
    img = np.zeros((300, 400, 3), dtype=np.uint8)
    img[:] = [50, 100, 150]  # Fill with a color

    # Add some text
    cv2.putText(img, 'Press any key to continue', (50, 150),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow('Static Image', img)
    print("Displaying image. Press any key to continue...")

    key = cv2.waitKey(0)  # Wait forever until a key is pressed
    print(f"You pressed key with code: {key}")

    cv2.destroyAllWindows()


def interactive_display():
    """Display camera feed with keyboard controls."""
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Could not open camera")
        return

    print("Camera feed with keyboard controls:")
    print("  'g' - Convert to grayscale")
    print("  'c' - Back to color")
    print("  's' - Save current frame")
    print("  'q' or ESC - Quit")
    print()

    grayscale_mode = False
    frame_count = 0

    while True:
        success, frame = camera.read()
        if not success:
            break

        # Apply grayscale if enabled
        if grayscale_mode:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)  # Convert back for display

        # Add mode indicator
        mode_text = "GRAYSCALE" if grayscale_mode else "COLOR"
        cv2.putText(frame, mode_text, (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Interactive Display', frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('g'):
            grayscale_mode = True
            print("Switched to grayscale")
        elif key == ord('c'):
            grayscale_mode = False
            print("Switched to color")
        elif key == ord('s'):
            filename = f'frame_{frame_count}.png'
            cv2.imwrite(filename, frame)
            print(f"Saved {filename}")
            frame_count += 1
        elif key == ord('q') or key == 27:  # 'q' or ESC
            print("Quitting...")
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    print("=== Part 1: Static Image Display ===")
    display_static_image()

    print()
    print("=== Part 2: Interactive Camera Display ===")
    interactive_display()
