import cv2
import mediapipe as mp


class VisionEngine:

    def __init__(self):

        self.camera = cv2.VideoCapture(0)

        # Camera settings
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)

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

        self.detector = HandLandmarker.create_from_options(options)

    def get_hand(self):

        success, frame = self.camera.read()

        if not success:
            return None

        # Mirror camera
        frame = cv2.flip(frame, 1)

        # Convert to RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb
        )

        result = self.detector.detect(mp_image)

        if not result.hand_landmarks:
            return None

        # Index fingertip
        fingertip = result.hand_landmarks[0][8]

        h, w, _ = frame.shape

        x = int(fingertip.x * w)
        y = int(fingertip.y * h)

        return (x, y)