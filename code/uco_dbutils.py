"""
Util methods for image and annotation files treatment
"""
import os
import numpy as np
import cv2

def parseFileLAEOframe(filename):
    """

    :param filename: annotations at frame level
    :return: the annotations
    """
    labels = -1
    if os.path.exists(filename):
        labels = np.loadtxt(filename, delimiter=" ", usecols=1)
    else:
        print('Error: cannot find file')

    return labels

def parseFileBBAnnotations(filename):
    """
    Aux method used to parse  bounding box annotations from file
    :param filename: File where bb annotations are stored
    :return Annotations list

    """
    lAnnotations = []
    annotation = []
    file = open(filename, "r")
    for line in file:
        ldata = line.split()
        if len(ldata) == 1:
            if len(annotation) > 0:
                lAnnotations.append(annotation)
            annotation = []
        else:
            if len(ldata) >= 4:
                annotation.append([[int(ldata[0]), int(ldata[1])], [int(ldata[2]), int(ldata[3])]])

    # Add last annotation to list
    if len(annotation) > 0:
        lAnnotations.append(annotation)
    file.close()
    return lAnnotations


def parseFileLAEOpair(filename):
    """
    Aux method used to parse LAEO annotations from file
    :param filename: File where LAEO annotations are stored
    :return Annotations list

    """
    lAnnotations = []
    annotation = []
    file = open(filename, "r")
    for line in file:
        ldata = line.split()
        if len(ldata) == 1:
            if len(annotation) > 0:
                lAnnotations.append(annotation)
            annotation = []
        else:
            if len(ldata) >= 2:
                annotation.append((int(ldata[0]), int(ldata[1])))

    # Add last annotation to list
    if len(annotation) > 0:
        lAnnotations.append(annotation)
    file.close()

    return lAnnotations


def get_cropped_head(ann_file, image, frame, head_size):
    """
    Aux method used to get cropped resized images from source image
    :param ann_file: File where bounding box annotations are stored
    :param image: Source image to be cropped
    :param frame: Frame or row in ann_file for selecting correct annotation
    :param head_size: Cropped image desired output size
    :return Cropped images list

    """
    crop_images = []
    file = ann_file
    if not os.path.exists(image):
        print("Image file not found: "+image)
        head_ann = []
        return crop_images, head_ann, [1,1]

    image = cv2.imread(image)
    imgsize = image.shape
    head_ann = parseFileBBAnnotations(file)
    if frame < len(head_ann):
        head_ann = head_ann[frame]
    else:
        print("ERROR: invalid index ({:d}) for head_ann (len={:d}), using file:\n{:s}".format(frame, len(head_ann), ann_file))
        head_ann = []
        return crop_images, head_ann, [1,1]

    for j in range(0, len(head_ann)):
        x = int(head_ann[j][0][0])
        xh = int(head_ann[j][1][0])
        y = int(head_ann[j][0][1])
        yh = int(head_ann[j][1][1])

        dist = max(xh-x, yh-y)

        crop_img0 = image[y:y+dist, x:x+dist]

        if crop_img0.size != 0:
            crop_img0 = cv2.resize(crop_img0, head_size)
        else:
            print("WARN: empty image crop [{:s}]: {}".format(__name__, dist))

        crop_images.append(crop_img0)

    return crop_images, head_ann, imgsize



def laeo_head(frame, head, laeo_ann_file=""):
    """
    Aux method used to return the class label from two images
    :param laeo_ann_file: File where LAEO pair annotations are stored
    :param head: Two sized tuple which represent the two head indexes
    :param frame: Frame or row in ann_file for selecting correct annotation
    :return 1 if the two images are LAEO, otherwise returns 0

    """
    if laeo_ann_file[-14:-6] == 'negative':
        return 0

    if not os.path.exists(laeo_ann_file):
        print("LAEO file not found")
        exit(-1)

    lHead = parseFileLAEOpair(laeo_ann_file)
    if lHead[frame] == head or lHead[frame] == [(head[0][1], head[0][0])]:
        return 1

    return 0
