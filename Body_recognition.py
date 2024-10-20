import cv2
import mediapipe as mp

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# Capture video feed
cap = cv2.VideoCapture(0)

# Define a function to recognize posture/gestures based on body landmarks
def recognize_posture(pose_landmarks):
    # Extract landmark coordinates
    landmarks = [(landmark.x, landmark.y, landmark.z) for landmark in pose_landmarks.landmark]

    # Example: Recognize simple posture like standing based on specific landmarks
    # You can build custom logic using landmarks indices for body parts such as shoulders, hips, etc.
    # For example, comparing the relative positions of landmarks can help you define posture.

    # For now, return a placeholder posture (this logic can be extended based on your needs)
    return "Dance!!!"

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the BGR image to RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False

    # Process the image and detect the pose landmarks
    results = pose.process(image)

    # Draw the pose landmarks
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.pose_landmarks:
        # Draw pose landmarks on the image
        mp_drawing.draw_landmarks(
            image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Recognize posture
        posture = recognize_posture(results.pose_landmarks)

        # Display recognized posture
        cv2.putText(image, posture, (50, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Pose Detection with Gesture Recognition', image)

    if cv2.waitKey(5) & 0xFF == 27:  # Press 'ESC' to exit
        break

cap.release()
cv2.destroyAllWindows()
