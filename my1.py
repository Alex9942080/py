import cv2
import mediapipe as mp
 
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()



video=cv2.VideoCapture('rtsp://192.168.1.168:554/stream_1')

#video=cv2.VideoCapture(0)


while True:
	check,frame=video.read()
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	height, width, _ = frame.shape
	result = face_mesh.process(frame)
	#print(result)
	try:
		for facial_landmarks in result.multi_face_landmarks:
			for i in range(0, 468):
				landmrk = facial_landmarks.landmark[i]
				locx = int(landmrk.x * width)
				locy = int(landmrk.y * height)
				cv2.circle(frame, (locx, locy), 1, (0, 200, 0), 0)
				cv2.imshow("Image", frame)
 
	except:
		cv2.imshow("Image", frame)
		key=cv2.waitKey(1)
	if key==ord('q'):
		break
 
video.release()
cv2.destroyAllWindows()
