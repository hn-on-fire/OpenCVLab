import cv2

cap = cv2.VideoCapture("C:/Users/CV Lab/Documents/210962092/Lab1/Resources/video.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('Vid', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
