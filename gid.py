from google_images_download import google_images_download
import sys

if len(sys.argv) == 1:
   print('no arguments passed')
   sys.exit()
elif len(sys.argv) < 4:
   print('not enough arguments passed')
   sys.exit()
   
print(">> Use gid to search for and download a square icon file \n--------------------------------------------------------- \nHint: the first argument is the search term, the second argument is the file extension (e.g png or svg or ico etc), the third argument is the file output directory \nExample: gid 'debian installer' svg /tmp \nContact developer: teloslinux@protonmail.com \n---------------------------------------------------------") 
   
arguments = {"keywords":sys.argv[1],"limit":1,"size":"icon","format":sys.argv[2],"aspect_ratio":"square","output_directory":sys.argv[3]}
response = google_images_download.download(arguments)

sys.exit()
