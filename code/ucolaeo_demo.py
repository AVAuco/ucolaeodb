# UCO-LAEO dataset
#
# Demo file for released dataset
#
# Citation:
# =========
# MJ Marin-Jimenez, V. Kalogeiton, P. Medina-Suarez, A. Zisserman.
# "LAEO-Net: revisiting people Looking At Each Other in videos"
# CVPR, 2019
#
# MJMJ/2019

#import os
import sys

sys.path.insert(0, ".")

from uco_dbutils import *


extract_frames = False

# ==================================
# Extract all frames from all videos
# ==================================
framesdir = os.path.join("..", "frames")

if extract_frames:
    videosdir = os.path.join("..", "videos")



    if not os.path.exists(framesdir):
        os.makedirs(framesdir)

    errcode = os.system("python uco_getFramesLower.py {} {}".format(videosdir, framesdir))
    print(errcode)


# ==================================
# Show annotations
# ==================================

targetvideo = "Got06"

# Annotations at frame level: any LAEO in this frame?
# ---------------------------------------------------
annotations_dir = os.path.join("..", "annotations", "annotations_frame")

file_laeo_frame_level = os.path.join(annotations_dir, targetvideo.lower()+".txt")
laeo_frame_level = parseFileLAEOframe(file_laeo_frame_level)

# Read frame
frame_id = 46 # 13 # Any in the video

imgname = os.path.join(framesdir, targetvideo.lower(), "{:06d}.jpg".format(frame_id))
img = cv2.imread(imgname)
if img is None:
    print("Image not found ({}). Have you extracted the frames?".format(imgname))
    exit(-1)

print("LAEO label at frame level: {}".format(int(laeo_frame_level[frame_id])))


# Annotations at head level: bounding-box
# ---------------------------------------------------
annotations_dir = os.path.join("..", "annotations", "annotations_head")

file_bbs = os.path.join(annotations_dir, targetvideo.lower()+"_heads.txt")
l_bbs = parseFileBBAnnotations(file_bbs)

l_bbs_this_frame = l_bbs[frame_id]
print("There are {:d} heads in this frame.".format(len(l_bbs_this_frame)))

for bix in range(0, len(l_bbs_this_frame)):
    cv2.rectangle(img, (l_bbs_this_frame[bix][0][0], l_bbs_this_frame[bix][0][1]),
                  (l_bbs_this_frame[bix][1][0], l_bbs_this_frame[bix][1][1]),
                  (255,64,0),3)


# LAEO annotations at head level: pairs
# ---------------------------------------------------
annotations_dir = os.path.join("..", "annotations", "annotations_pair")

file_pairs = os.path.join(annotations_dir, "pair_" + targetvideo.lower()+ ".txt")
l_pairs = parseFileLAEOpair(file_pairs)

pairs_this_frame = l_pairs[frame_id]   # VERY IMPORTANT: Note that heads are 1-indexed

npairs = len(pairs_this_frame)

for pix in range(0, npairs):
    pair = pairs_this_frame[pix]

    if pair[0] == -1 and pair[1] == -1:
        print("There are not LAEO pairs in this frame.")
        break

    print("Heads {} and {} are LAEO".format(pair[0], pair[1]))

    p1 = (l_bbs_this_frame[pair[0]-1][0][0], l_bbs_this_frame[pair[0]-1][0][1])
    p2 = (l_bbs_this_frame[pair[1]-1][0][0], l_bbs_this_frame[pair[1]-1][0][1])

    cv2.line(img, p1, p2, (0,255,0), 3)

cv2.imshow("Frame-{}".format(frame_id), img)
cv2.waitKey()

print("Done!")
