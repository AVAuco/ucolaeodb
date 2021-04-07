# UCO-LAEO: an annotated database for training and evaluating LAEO models

<div align="center">
    <img src="./ucolaeodb_samples.jpg" alt="UCO-LAEO database" width="640">
</div>

### Description 
We use four popular TV shows: ‘Game of thrones’, ‘Mr Robot’, ‘Silicon Valley’ and ‘The walking dead’. From these shows, we collect 129 (3-12 seconds long) shots and first annotate all the heads
in each frame with bounding boxes, and then annotate each head pair as LAEO or not-LAEO.

If you use this dataset in your work, please, cite [1][2].

### Download
The **extracted frames and annotations** are available at the following [URL](http://rabinf24.uco.es/ucolaeo/ucolaeodb_v1.1.tgz).    
To download the **videos**, use the following [URL](http://rabinf24.uco.es/ucolaeo/ucolaeodb_videos_v1.1.tgz). 

Alternatively, you can download and extract the videos, annotations and frames using: 

    curl http://rabinf24.uco.es/ucolaeo/ucolaeodb_v1.1.tgz | tar xz
    curl http://rabinf24.uco.es/ucolaeo/ucolaeodb_videos_v1.1.tgz | tar xz

### Annotations
The dataset contains 3 types of annotations:
 + Frame-level LAEO: is there any pair of people LAEO?
 + Head bounding-boxes: for each frame and each visible head, bouding boxes are provided.
 + Pair-level LAEO: for each frame, those pairs of heads that are LAEO are indicated. 

**WARNING**: all the annotations fit the provided frames. Therefore, there might exist some misalignment with respect to the video files.

### Code
After downloading the package containing the videos and annotations, within the `code` directory, run `ucolaeo_demo.py` for a quick example.

### Evaluation protocol
The file `code/uco_dbconfig.py` contains information about the videos used for validation and testing at [1][2], the remaining ones were used for training.

### References
[1]
```
@inproceedings{marin21pami,
  author    = {Mar\'in-Jim\'enez, Manuel J. and Kalogeiton, Vicky and Medina-Su\'arez, Pablo and and Zisserman, Andrew},
  title     = {{LAEO-Net++}: revisiting people {Looking At Each Other} in videos},
  booktitle = TPAMI,
  year      = {2021}
}
```
[2]
```
@inproceedings{marin19cvpr,
  author    = {Mar\'in-Jim\'enez, Manuel J. and Kalogeiton, Vicky and Medina-Su\'arez, Pablo and and Zisserman, Andrew},
  title     = {{LAEO-Net}: revisiting people {Looking At Each Other} in videos},
  booktitle = CVPR,
  year      = {2019}
}
```

### Acknowledgments

The initial version of this dataset was compiled by Rafael Fernandez during the development of his final project (IT degree) at the [University of Cordoba](http://www.uco.es/investiga/grupos/ava/node/42).   
Thanks to [RSKothari](https://github.com/RSKothari) for detecting the frames' mismatch and to [Isabel Jimenez](https://github.com/IsabelJimenez99) for fixing it.

