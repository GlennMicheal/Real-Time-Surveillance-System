# Multiple camera streaming (Example: Camera 1 and Camera 2)
cap1 = cv2.VideoCapture(0)  # Camera 1
cap2 = cv2.VideoCapture(1)  # Camera 2

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        break

    # Display the frames from both cameras
    combined_frame = np.hstack((frame1, frame2))
    cv2.imshow("Multi-Camera Surveillance", combined_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
