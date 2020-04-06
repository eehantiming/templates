'''
Press spacebar to capture images. 
Creates a dir to hold the images.
'''

import cv2
import os
import time

# path = 'Josh_2-15-2020_24726510.png'
# image = cv2.imread(path)

# while True:
# 	cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# 	cv2.imshow('image', image)
# 	k = cv2.waitKey(0)
# 	if k == ord('q'):
# 		break

savedir = os.getcwd() + '/captures'
count = 0
cap = cv2.VideoCapture(0)
width = cap.get(3)
height = cap.get(4)
print(f'video reso is {width} by {height}')

while cap.isOpened():
	ret, frame = cap.read()
	cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
	cv2.imshow('Video', frame)
	k = cv2.waitKey(16)
	if k == ord('q'):
		break
	if k == 32: # spacebar
		# cv2.imwrite(savepath, frame)
		if not os.path.exists(savedir):
			os.mkdir(savedir)
			time.sleep(2)
			print(f'Created {savedir}!')
			cv2.imwrite(f'{savedir}/{count}.jpg', frame)
		elif os.path.exists(f'{savedir}/{count}.jpg'):
			count += 1
		else: 
			print(f'{savedir}/{count}.jpg')
			cv2.imwrite(f'{savedir}/{count}.jpg', frame)

cap.release()
cv2.destroyAllWindows()