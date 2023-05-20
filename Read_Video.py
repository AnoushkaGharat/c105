import cv2

wid = cv2.VideoCapture("AnthonyShkraba.mp4")

if(wid.isOpened()==False):
    print("Unable to read feed")

height = int(wid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)
width = int(wid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)
fps=int(wid.get(cv2.CAP_PROP_FPS))
print(fps)

out=cv2.VideoWriter("boxing.mp3",cv2.VideoWriter_fourcc(*"DIVX"),30,(width,height))
while(True):
    ret,frame=wid.read()
    cv2.imshow("webcam",frame)
    out.write(frame)
    if cv2.waitKey(25)==32:
        break
    
    
cv2.waitKey(0)
wid.release()
cv2.destroyAllWindows()