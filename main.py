import cv2
def take_Snapshots():
    vco=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=vco.read()
        cv2.imwrite("1.jpg",frame)
        result=False
    vco.release()
    cv2.destroyAllWindows()
take_Snapshots()