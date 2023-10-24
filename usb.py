import shutil
import os
import time
path_to_check = r'D:'

while True:
	if os.path.exists(path_to_check): 
		print("usb takıldı")
		time.sleep(1)
		usb_file = r'D:'
		source_folder = usb_file
		destination_folder = 'usbcontent'
		shutil.copytree(source_folder, destination_folder)
		break
	else:
		print("usb yi tak")
		pass