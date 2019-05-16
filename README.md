# UCO-LAEO: an annotated database for training and evaluating LAEO models

<div align="center">
    <img src="./ucolaeodb_samples.jpg" alt="UCO-LAEO database" width="640">
</div>

### Description 
We use four popular TV shows: ‘Game of thrones’, ‘Mr Robot’, ‘Smallville’ and ‘The walking dead’. From these shows, we collect 129 (3-12 seconds long) shots and first annotate all the heads
in each frame with bounding boxes, and then annotate each head pair as LAEO or not-LAEO.

If you use this dataset in your work, please, cite [1].

### Download
The **videos and annotations** are available at the following [URL](http://rabinf24.uco.es/ucolaeo/ucolaeodb.tgz)    
To download the already **extracted frames**, use the following [URL](http://www.robots.ox.ac.uk/~vgg/research/laeonet/downloads/UCOLAEO_v1.0_frames.tar.gz)

### Annotations
The dataset contains 3 types of annotations:
 + Frame-level LAEO: is there any pair of people LAEO?
 + Head bounding-boxes: for each frame and each visible head, bouding boxes are provided.
 + Pair-level LAEO: for each frame, those pairs of heads that are LAEO are indicated. 
 
### Code
After downloading the package containing the videos and annotations, within the `code` directory, run `ucolaeo_demo.py` for a quick example.

### Evaluation protocol
The file `code/uco_dbconfig.py` contains information about the videos used for validation and testing at [1], the remaining ones were used for training.

### References
[1]
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
