import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

#  for nn in range(1, 3): print(nn)

# For webcam input:
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
cap = cv2.VideoCapture(0)
with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as face_mesh:
  while cap.isOpened():
    success, image = cap.read()

    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue


    height, width, channels = image.shape
    # print(image.shape)
   #  print(
   #         f"width: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}, height:   #{cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}, fps: {cap.get(cv2.CAP_PROP_FPS)}")

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # cv2.threshold(image, 150, 200, 10) # только для серого

    results = face_mesh.process(image)

  # for facial_landmarks in result.multi_face_landmarks:
    #  for i in range(0, 468):
     #     pt1 = facial_landmarks.landmark[3]
      #    x = int(pt1.x * width)
      #    y = int(pt1.y * height)
       #   cv2.circle(image, (x, y), 5, (100, 100, 0), -1)


    # Draw the face mesh annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

##    if results.multi_face_landmarks != None:
##        for face_landmarks in results.multi_face_landmarks:
##            mp_face_mesh.draw_landmarks(
##              image, faceLandmarks,
##            faceModule.FACE_CONNECTIONS,
##              circleDrawingSpec,
##              lineDrawingSpec)

  if results.multi_face_landmarks:
       for face_landmarks in results.multi_face_landmarks:
##           mp_drawing.draw_landmarks(
##               image=image,
##               landmark_list=face_landmarks,
##               connections=mp_face_mesh.FACEMESH_TESSELATION,
##               landmark_drawing_spec=None,
##               connection_drawing_spec=mp_drawing_styles
##               .get_default_face_mesh_tesselation_style())
##            mp_drawing.draw_landmarks(
##                image=image,
##                landmark_list=face_landmarks,
##                connections=mp_face_mesh.FACEMESH_CONTOURS,
##                landmark_drawing_spec=None,
##                connection_drawing_spec=mp_drawing_styles
##                .get_default_face_mesh_contours_style())
##           mp_drawing.draw_landmarks(
##               image=image,
##               landmark_list=face_landmarks,
##               connections=mp_face_mesh.FACEMESH_IRISES,
##               landmark_drawing_spec=None,
##               connection_drawing_spec=mp_drawing_styles
##               .get_default_face_mesh_iris_connections_style())
           mp_drawing.draw_landmarks(
               image=image,
               landmark_list=face_landmarks,
               connections=mp_face_mesh.FACE_CONNECTIONS,
               landmark_drawing_spec=None,
               connection_drawing_spec=mp_drawing_styles
               .get_default_face_mesh_iris_connections_style())

##    print(results.multi_face_landmarks[0].landmark[66])
  if cv2.waitKey(5) & 0xFF == 27:
break

cap.release()


