from __future__ import division, print_function
import cv2
import platform
import os


def videoWrite(frames, fname='out.mp4', fps=30):
    shape = frames[0].shape
    
    frame_height, frame_width = shape[:2]
    
    # video writer doesn't like grayscale images, have
    # to convert to RGB
    if len(shape) == 2:
        grayscale = True
    else:
        grayscale = False
    
    # pick a good encoder for the current OS
    sys = platform.system().lower()
    if sys in ['darwin']:
        fourcc = 'avc1'
    else:
        fourcc = 'mjpg'
    
    print('>> Saving {} {}x{} images to {}'.format(len(imgs), shape[1], shape[0], fname))
    print('>> using {} on {}'.format(fourcc, sys))
    
    # create the video writer and write all frames to the file
    out = cv2.VideoWriter(
        fname,
        cv2.VideoWriter_fourcc(*fourcc), 
        fps, 
        (frame_width,frame_height))
    
    for frame in frames:
        # convert if necessary to RGB
        if grayscale:
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
        out.write(frame)
    
    out.release()
    print('>> wrote {:.1f} MB'.format(os.path.getsize(fname)/(1E6)))
