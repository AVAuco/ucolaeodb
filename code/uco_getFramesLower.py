#----------
# This simple script gets all frames from all mp4 files in a source directory
# Run with: 'python getFramesLower.py [sourceDir] [destDir]'
# Lower-case version of names
#----------

import cv2
import os
import glob
import sys

if(len(sys.argv)<3):
    print("ERROR Need to specify <SourceDir> <DestDir> [<VideoPatt:*.mp4>]")
    exit()

sourceDir=sys.argv[1]
destDir=sys.argv[2]

if len(sys.argv) > 3:
    filePatt= sys.argv[3]
else:
    filePatt="*.mp4"

if not(os.path.isdir(sourceDir) and os.path.isdir(destDir)):
     print("ERROR Directory not found: {}".format(destDir))
     exit()

#Get all mp4 files in source directory
allFiles = glob.glob(os.path.join(sourceDir, filePatt))
allFiles = sorted(allFiles)
nfiles = len(allFiles)
print('* Found:', nfiles)


for file in allFiles:
    print(file)
    vidcap = cv2.VideoCapture(file)

    # Get file name w/o extension
    namefile = os.path.splitext(os.path.basename(file))[0]
    namefile = namefile.lower()
    success,image = vidcap.read()
    count = 0

    outdir = destDir + "/%s" % namefile
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    # Folder route where frames will be stored
    while success:

        outname = destDir + "/%s/%06d.jpg" % (namefile, count)
        cv2.imwrite(outname, image)

    #Press ESC at anytime to quit program
        if cv2.waitKey(10) == 27:
          break
        count += 1
        success, image = vidcap.read()