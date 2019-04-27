# Progress Bar #


Implementation of a generic progress bar for loops inspired by keras.  
Displays progress, an estimate of time to complete, with total time and time per step at the end.
Optionally statistics formatted as string can be included.
Example:

8074/10000 [========================>.....] - ETA: 1s
10000/10000 [==============================] - 7s 768us/step

### Set up ###

Copy the file pbar.py to the working directory for your project
If there is interest I might make a pip installer

run pbar.py to see a demo

### Usage ###

	from pbar import ProgressBar
	LOOP_LENGTH = 50
	pb = ProgressBar(LOOP_LENGTH)  # optional ProgressBar(LOOP_LENGTH, update_every = 0.5) to update every 0.5 seconds, default 0.1
	for i in range(LOOP_LENGTH):
		... do stuff ...
		pb.show()    # optional pbar.show(i+1, stats = 'some statistics formatted as string')
		
	pb.reset()  # to reset for next loop.  Optional pbar.reset(total = LOOP_LENGTH, update_every = 0.5)

