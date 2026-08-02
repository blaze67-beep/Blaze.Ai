import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)


def get_hand_position():
    success, frame = cap.read()

    if not success:
        return None

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    if results.multi_hand_landmarks:

        hand = results.multi_hand_landmarks[0]

        index = hand.landmark[8]

        h, w, _ = frame.shape

        x = int(index.x * w)
        y = int(index.y * h)

        return x, y

    return None