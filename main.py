import sys
import os
import cv2

if len(sys.argv) != 3:
    print("Usage: python3 <rollno>.py <path/to/slides/directory> <path/to/frames/directory>")
    sys.exit(1)

args = sys.argv
slides_dir = args[1]
frames_dir = args[2]
slides_files = os.listdir(slides_dir)
frames_files = os.listdir(frames_dir)

answer_file = open("ans.txt", 'w')

for frame in frames_files:
    frm = frames_dir + "/" + frame
    f = cv2.imread(frm)
    max_match = 0
    for slide in slides_files:
        sld = slides_dir + "/" + slide
        s = cv2.imread(sld)
        match = cv2.matchTemplate(f, s, cv2.TM_CCORR_NORMED)
        if match > max_match:
            max_match = match
            slide_max = slide
    answer_file.write(frame + " " + slide_max + "\n")  
