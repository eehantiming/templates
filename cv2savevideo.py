'''
Creates a dir to hold videos. 
Press space bar to start recording. Press space bar again to pause/resume.
Press q to exit, a mp4 video will be saved in folder.
'''
import cv2
import os
import time

savedir = os.getcwd() + '/videos'
count = 0

cap = cv2.VideoCapture(0) #  or put video file name as string 
width = int(cap.get(3))
height = int(cap.get(4))
print(f'video reso is {width} by {height}')

if not os.path.exists(savedir):
	os.mkdir(savedir)
	print(f'Created {savedir}!')
	time.sleep(2)

while os.path.exists(f'{savedir}/{count}.mp4'):
	count += 1

out = cv2.VideoWriter(f'{savedir}/{count}.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 15.0, (width, height))
print(f'Press spacebar to record video at:{savedir}/{count}.mp4')
record = False

while cap.isOpened():
	ret, frame = cap.read()

	if record:
		out.write(frame)

	cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
	cv2.imshow('Video', frame)
	k = cv2.waitKey(16)
	if k == ord('q'):
		break
	if k == 32: # spacebar
		record = not record
		print(f'Recording: {record}')

cap.release()
out.release()
cv2.destroyAllWindows()