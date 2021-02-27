#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 23:13:32 2018

@author: Prashant Bhat

Script extract the frames from video

Make sure to confirm this - OUTPUT_FRAMES_PER_SECOND can add or reduce the blur
"""


import cv2
import os
import math
from glob import glob

INPUT_VIDEO_PATH = r'D:/AI_usecase_ML_Models/steering_bypass_pin/data/raw_data/video/trim_videos'
INPUT_VIDEO_FORMAT = 'mp4' # chage for differnce extension
FRAME_OUTPUT_DIRECTORY_PATH = r'D:/AI_usecase_ML_Models/steering_bypass_pin/data/raw_data/video_frames'
# OUTPUT_FILE_PREFIX = 'v9-apple_out_top_right-30'
OUTPUT_FORMAT = 'jpg'
OUTPUT_FRAMES_PER_SECOND = 5  # Set the variable to None to extract all the frames every second


def output_frames(input_video_path, output_dir_path, out_file_prefix, output_format, output_frames_per_second):
    print('Loading Video {}...'.format(input_video_path))
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)
    video_capture = cv2.VideoCapture(input_video_path)
    frame_rate = video_capture.get(5)  # Get frame rate

    if output_frames_per_second is not None and output_frames_per_second > frame_rate:
        raise Exception('The video has a frame rate of {} fps. The value of OUTPUT_FRAMES_PER_SECOND must be less than or equal to the frame rate. Currently it is {}.'.format(int(frame_rate), output_frames_per_second))

    if video_capture.isOpened():
        print('Video Loaded Successfully')

    count = 0

    while video_capture.isOpened():
        frame_id = int(video_capture.get(1))  # Current frame number
        success, image = video_capture.read()

        if not success:
            break

        if output_frames_per_second is None:
            required_frames = 1
        else:
            required_frames = int(math.floor(frame_rate / output_frames_per_second))

        if frame_id % required_frames == 0:
            output_path = os.path.join(output_dir_path,
                                       '{}-{}.{}'.format(out_file_prefix, count, output_format))
            print('Writing Frame: {}'.format(output_path))
            cv2.imwrite(output_path, image)     # save frame as JPEG file
            count += 1

    print('All Frames Extracted Successfully')

def main():    
    for filepath in glob(os.path.join(INPUT_VIDEO_PATH, '*.' + INPUT_VIDEO_FORMAT)):
        fname_ext = os.path.basename(filepath)
        fname, ext = os.path.splitext(fname_ext)
        output_path = os.path.join(FRAME_OUTPUT_DIRECTORY_PATH, fname + '-' + str(OUTPUT_FRAMES_PER_SECOND))
        output_frames(filepath, output_path, fname, OUTPUT_FORMAT, OUTPUT_FRAMES_PER_SECOND)
        print('-' * 40)
main()