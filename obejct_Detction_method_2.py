import cv2

cap = cv2.VideoCapture('/home/ksuser/LS/Yolonas-deepsort/cctv_footage/pathway_2/pathway_2.mp4')

object_detector = cv2.createBackgroundSubtractorMOG2()


while True:
    ret, frame = cap.read()
    
    #obejct Detection 
    mask = object_detector.apply(frame)
    
    contours, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        
        if area > 100:
            cv2.drawContours(frame, [cnt], -1, (0,255,0))
            
    
    cv2.imshow('Frame', cv2.resize(frame,(1280,720)))
    cv2.imshow('Mask', cv2.resize(mask,(1280,720)))
    
    key = cv2.waitKey(30)
    
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows