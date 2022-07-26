#creating image data

import os
import subprocess
import glob

my_path = "/content/drive/MyDrive/retrospective cycle GAN/UCF-101/vid_data"
# files = glob.glob(my_path + r'//*//*.avi', recursive=True) #we have 13207 folders
files = glob.glob(my_path + r'//*//', recursive=True )[1:2]

for VidClass in files:
  video_files = glob.glob(VidClass + r'*.avi', recursive=True)
  for vidItem in video_files:
      path = os.path.splitext(vidItem)[0]
      store_pth = path.replace("vid_data", "img_data")
      if not os.path.exists(store_pth):
          os.makedirs(store_pth)
      

      vidItem = vidItem.split('/')[-4:]
      vidItem = os.path.join(*vidItem)

      store_pth = os.path.splitext(store_pth)[0].split('/')[-4:]
      store_pth = os.path.join(*store_pth)

      query = "ffmpeg -i " + vidItem + " -r 20 " + store_pth + "//pic%04d.jpg -hide_banner"
      response = subprocess.Popen(query, shell=True, stdout=subprocess.PIPE).stdout.read()
      s = str(response).encode('utf-8')

