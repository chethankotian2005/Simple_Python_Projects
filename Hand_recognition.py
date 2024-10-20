import cv2
import mediapipe as mp

# Initialize MediaPipe Hand
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Capture video feed
cap = cv2.VideoCapture(0)

# Define a function to recognize gestures
def recognize_gesture(hand_landmarks):
    # Extract landmark coordinates
    landmarks = [(landmark.x, landmark.y, landmark.z) for landmark in hand_landmarks.landmark]

    # Calculate bounding box
    min_x = min(landmark[0] for landmark in landmarks)
    max_x = max(landmark[0] for landmark in landmarks)
    min_y = min(landmark[1] for landmark in landmarks)
    max_y = max(landmark[1] for landmark in landmarks)

    # Convert bounding box to pixel coordinates
    bbox = [
        int(min_x * image.shape[1]),
        int(min_y * image.shape[0]),
        int((max_x - min_x) * image.shape[1]),
        int((max_y - min_y) * image.shape[0])
    ]

    # Recognize gestures based on landmarks
    if len(landmarks) == 21:  # Assuming it's a full hand detected
    # Check for extended fingers
        extended_fingers = 0
    
    # Thumb
        if landmarks[4][1] < landmarks[3][1]:  # Thumb tip (landmarks[4]) above index finger (landmarks[3])
            extended_fingers += 1
    
    # Index finger
        if landmarks[8][1] < landmarks[6][1]:  # Index finger tip (landmarks[8]) above knuckle (landmarks[6])
            extended_fingers += 1
    
    # Middle finger
        if landmarks[12][1] < landmarks[10][1]:  # Middle finger tip (landmarks[12]) above knuckle (landmarks[10])
            extended_fingers += 1
    
    # Ring finger
        if landmarks[16][1] < landmarks[14][1]:  # Ring finger tip (landmarks[16]) above knuckle (landmarks[14])
            extended_fingers += 1
    
    # Little finger
        if landmarks[20][1] < landmarks[18][1]:  # Little finger tip (landmarks[20]) above knuckle (landmarks[18])
            extended_fingers += 1


        # Gesture recognition
        if extended_fingers == 0:
            return "Fist"  # Gesture for 0 or Fist
        elif extended_fingers == 1:
            return "1"
        elif extended_fingers == 2:
            return "2"
        elif extended_fingers == 3:
            return "3"
        elif extended_fingers == 4:
            return "4"
        elif extended_fingers == 5:
            return "5"
        

    return None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the BGR image to RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False

    # Process the image and detect the hand landmarks
    results = hands.process(image)

    # Draw the hand landmarks and bounding box
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw bounding box
            min_x = min(hand_landmarks.landmark, key=lambda landmark: landmark.x).x
            max_x = max(hand_landmarks.landmark, key=lambda landmark: landmark.x).x
            min_y = min(hand_landmarks.landmark, key=lambda landmark: landmark.y).y
            max_y = max(hand_landmarks.landmark, key=lambda landmark: landmark.y).y

            bbox = [
                int(min_x * image.shape[1]),
                int(min_y * image.shape[0]),
                int((max_x - min_x) * image.shape[1]),
                int((max_y - min_y) * image.shape[0])
            ]

            cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (255, 0, 0), 2)

            # Draw hand landmarks within the bounding box
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Recognize gesture
            gesture = recognize_gesture(hand_landmarks)

            # Display gesture number
            if gesture:
                cv2.putText(image, gesture, (bbox[0], bbox[1] - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Hand Tracking with Gesture Recognition', image)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
