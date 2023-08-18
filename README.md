
# Object Detection in Hyperspectral Image via Unified Spectral-Spatial Feature Aggregation

This repo is the official implementation for **Object Detection in Hyperspectral Image via Unified Spectral-Spatial Feature Aggregation**. The paper has been accepted to **TGRS 2023**.

### News

[2023.08.18] Our paper is ready!


## Installation 
Python>=3.6.0 is required with all requirements.txt installed including PyTorch>=1.7 (The same as yolov5 https://github.com/ultralytics/yolov5 ).

  
#### Install requirements
 ```bash
$ pip install -r requirements.txt
```


# HSI-Object-Detection

We provide processed spectral aggregation information and spatial aggregation information in the data set.

If you were to reprocess hyperspectral data, the original hyperspectral data needs to be processed before they can use, reference: https://www.hsitracking.com/.

## Dataset
### HOD3K

Contains the raw hyperspectral train:

-[HOD3K]  [download](https://pan.baidu.com/s/16ofE5ljzvNCFU_NO43xE6Q) password:gvbe

Contains the processed hyperspectral dataset and the raw hyperspectral val and test dataset:

-[HOD3K]  [download](https://pan.baidu.com/s/1ga-YqLqTqVxTbnHHjch82g) password:qugy



### HSI-1
[download](https://github.com/yanlongbinluck/HSI-Object-Detection-NPU)

### Lable

In the HSI-1 dataset, you need to convert all annotations to YOLOv5 format.

Refer: https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data

### Visualization of HOD3K Dataset
 
<div align="left">
<img src="https://github.com/hexiao-cs/S2ANet/blob/main/img_readme/show.png" width="800">
</div>

## Run
#### Download the pretrained weights
yolov5 weights (pre-train) 

-[yolov5s] [google drive](https://drive.google.com/file/d/1UGAsaOvV7jVrk0RvFVYL6Vq0K7NQLD8H/view?usp=sharing)

-[yolov5m] [google drive](https://drive.google.com/file/d/1qB7L2vtlGppGjHp5xpXCKw14YHhbV4s1/view?usp=sharing)

-[yolov5l] [google drive](https://drive.google.com/file/d/12OFGLF73CqTgOCMJAycZ8lB4eW19D0nb/view?usp=sharing)

-[yolov5x] [google drive](https://drive.google.com/file/d/1e9xiQImx84KFQ_a7XXpn608I3rhRmKEn/view?usp=sharing)



### Train Test and Detect
train: ``` python train.py```

test: ``` python test.py```

detect: ``` python detect_twostream.py```

### S2ADet Overview
<div align="left">
<img src="https://github.com/hexiao-cs/S2ANet/blob/main/img_readme/backbone.png" width="800">
</div>

### Visualization of Detection

<div align="left">
<img src="https://github.com/hexiao-cs/S2ANet/blob/main/img_readme/showtime.png" width="800">
</div>

#### References

https://github.com/ultralytics/yolov5


