import time
import os
import sys
import random
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source = r"C:\Users\Nikhil\Downloads\sample"
destination=r"C:\Users\Nikhil\Downloads\sample - Copy"

dictType = {
  "Image_Files": ['.jpg', '.png','.gif','.tiff','.jpeg'],
  "Video_Files": ['.avi', '.mp4', '.webm', '.mp2', '.mpv', '.wmv', '.mpeg'],
  "Document_Files": ['.ppt', '.pdf', '.xls', '.csv', '.txt', '.xlsx'],
  "Audio_Files":['.mp3','.adts'],
  "Setup_Files": [".exe", ".bin", ".cmd", ".msi", ".dmg"]
}

class FileMovementHandler(FileSystemEventHandler):
  def on_create(self,event):
    name,extension=os.path.splitext(event.src_path)
    time.sleep(1)
    for key,value in dictType.items():
      time.sleep(1)
      if extension in value:
        file_name=os.path.basename(event.src_path)
        print("Downloading..."+ file_name)
        # path1: "C:\Users\Nikhil\Downloads\sample" + "file_name"
        # path2: "C:\Users\Nikhil\Downloads\sample-copy" + "Image_Files"
        # path3: "C:\Users\Nikhil\Downloads\sample-copy" +  "Image_Files" + "file_name"
        path1 = source + "/"+file_name
        path2= destination+'/'+key
        path3= destination+'/'+key+'/'+file_name
        
        if os.path.exists(path2):
          print("dict exists")
          print("Moving"+ file_name+" ....")
          shutil.move(path1,path3)
          time.sleep(1)
          
        else:
          print("Making new dir...")
          os.makedirs(path2)
          print("Moving"+ file_name+" ....")
          shutil.move(path1,path3)
          time.sleep(1)

Handler= FileMovementHandler()
myObserver= Observer()
myObserver.schedule(Handler,source,recursive=True)
myObserver.start()

try:
  while True:
    time.sleep(1)
    print("Handling Files....")
    
except KeyboardInterrupt:
  print("Stopping")
  myObserver.stop()