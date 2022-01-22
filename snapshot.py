import cv2
def take_snapshot():
    VideoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=VideoCaptureObject.read()
        cv2.imwrite("new Picture 1.jpg",frame)
        result=False
        VideoCaptureObject.release()
        cv2.destroyAllWindows()
take_snapshot()