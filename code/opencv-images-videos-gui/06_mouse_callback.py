"""
Mouse Callbacks: Handling mouse input in OpenCV windows.

This script demonstrates:
- Registering mouse callbacks with setMouseCallback
- Responding to different mouse events (click, move, drag)
- Building a simple drawing application
"""

import cv2
import numpy as np


# Global variables for the drawing app
drawing = False
last_point = None
canvas = None


def simple_click_callback(event, x, y, flags, param):
    """Simple callback that prints click coordinates."""
    if event == cv2.EVENT_LBUTTONUP:
        print(f"Left-click at ({x}, {y})")
    elif event == cv2.EVENT_RBUTTONUP:
        print(f"Right-click at ({x}, {y})")
    elif event == cv2.EVENT_MBUTTONUP:
        print(f"Middle-click at ({x}, {y})")


def drawing_callback(event, x, y, flags, param):
    """Callback for drawing on the canvas."""
    global drawing, last_point, canvas

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        last_point = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing and last_point is not None:
            cv2.line(canvas, last_point, (x, y), (0, 255, 0), 2)
            last_point = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        last_point = None


def demo_simple_clicks():
    """Demo: Simple click detection."""
    print("=== Simple Click Demo ===")
    print("Click anywhere in the window. Press 'q' to continue.")
    print()

    img = np.zeros((400, 600, 3), dtype=np.uint8)
    img[:] = [40, 40, 40]

    cv2.putText(img, 'Click anywhere!', (150, 200),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(img, "Press 'q' to continue", (150, 250),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (150, 150, 150), 1)

    cv2.namedWindow('Click Demo')
    cv2.setMouseCallback('Click Demo', simple_click_callback)

    while True:
        cv2.imshow('Click Demo', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyWindow('Click Demo')


def demo_drawing_app():
    """Demo: Simple drawing application."""
    global canvas

    print()
    print("=== Drawing App Demo ===")
    print("Draw by holding left mouse button and dragging.")
    print("Press 'c' to clear, 'q' to quit.")
    print()

    canvas = np.zeros((400, 600, 3), dtype=np.uint8)
    canvas[:] = [255, 255, 255]  # White background

    cv2.namedWindow('Drawing App')
    cv2.setMouseCallback('Drawing App', drawing_callback)

    while True:
        cv2.imshow('Drawing App', canvas)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('c'):
            canvas[:] = [255, 255, 255]
            print("Canvas cleared")
        elif key == ord('q'):
            break

    cv2.destroyWindow('Drawing App')


def demo_camera_with_clicks():
    """Demo: Camera feed where clicks mark points."""
    print()
    print("=== Camera Click Demo ===")
    print("Click on the camera feed to mark points.")
    print("Press 'c' to clear marks, 'q' to quit.")
    print()

    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Error: Could not open camera")
        return

    points = []

    def camera_click_callback(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONUP:
            points.append((x, y))
            print(f"Marked point at ({x}, {y})")

    cv2.namedWindow('Camera Clicks')
    cv2.setMouseCallback('Camera Clicks', camera_click_callback)

    while True:
        success, frame = camera.read()
        if not success:
            break

        # Draw all marked points
        for point in points:
            cv2.circle(frame, point, 5, (0, 0, 255), -1)
            cv2.circle(frame, point, 10, (0, 0, 255), 2)

        cv2.imshow('Camera Clicks', frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('c'):
            points.clear()
            print("Points cleared")
        elif key == ord('q'):
            break

    camera.release()
    cv2.destroyWindow('Camera Clicks')


if __name__ == '__main__':
    demo_simple_clicks()
    demo_drawing_app()
    demo_camera_with_clicks()
    print()
    print("Done!")
