# Using a background subtractor to detect motion
fgbg = cv2.createBackgroundSubtractorMOG2()

cap = cv2.VideoCapture("video_source.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Apply background subtraction
    fgmask = fgbg.apply(frame)

    # Find contours of moving objects
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Minimum area threshold for motion
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # Proactively flagging suspicious motion
            cv2.putText(frame, "Suspicious Motion Detected", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
    
    cv2.imshow("Proactive Crime Prevention", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
