from operator import truediv
import cv2
import dropbox
import time
import random
start_time=time.time()
def  take_Snapshots():
    number=random.randint(0,1000)
    video=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=video.read()
        imt_name="img"+str(number)+".png"
        cv2.imwrite(imt_name,frame)
        start_time=time.time
        result=False
    return imt_name
    print("Snapshot Was Taken")
    video.release()
    cv2.destroyAllWindows()
def upload_Files(imt_name):
    access_token='Wxkrb4NY6kwAAAAAAAAAAYHNQNTKu4D34GQ2GE0lXaJcGUm-HP0f3_hU9vPD0kXY'
    file=imt_name
    file_from=file
    file_to="/testfolder/"+(imt_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")
def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_Snapshots()
            upload_Files(name)
main() 
        
    