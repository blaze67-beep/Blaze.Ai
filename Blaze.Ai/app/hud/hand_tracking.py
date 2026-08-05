import cv2
import mediapipe as mp

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path="models/mediapipe/hand_landmarker.task"
    ),
    running_mode=VisionRunningMode.IMAGE,
    num_hands=1
)

detector = HandLandmarker.create_from_options(options)

camera = cv2.VideoCapture(0)


def get_hand_position():
    success, frame = camera.read()

    if not success:
        return None

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    result = detector.detect(mp_image)

    cv2.imshow("Camera Test", frame)
    cv2.waitKey(1)

    if not result.hand_landmarks:
        return None

    h, w, _ = frame.shape

    index_tip = result.hand_landmarks[0][8]

    x = int(index_tip.x * 500)
    y = int(index_tip.y * 500)

    print(f"Hand: {x}, {y}")

    return (x, y)