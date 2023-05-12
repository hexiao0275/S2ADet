# Multispectral-Object-Detection

We have released our dataset proposed in paper 'Object Detection in Hyperspectral Images'. Raw hyperspectral images and processed data (96-channel) can be found at [baidu cloud, password: 6shr], [Onedrive].

## Abstract

### Overview
<div align="left">
<img src="https://github.com/hexiao-cs/S2ANet/blob/main/img_readme/backbone.png" width="800">
</div>

### Visualization of Detection

<div align="left">
<img src="https://github.com/hexiao-cs/S2ANet/blob/main/img_readme/showtime.png" width="800">
</div>

### Visualization of HOD3K Dataset
 
<div align="left">
<img src="https://github.com/hexiao-cs/S2ANet/blob/main/img_readme/show.png" width="800">
</div>


## Installation 
Python>=3.6.0 is required with all requirements.txt installed including PyTorch>=1.7 (The same as yolov5 https://github.com/ultralytics/yolov5 ).

#### Clone the repo
    git clone https://github.com/DocF/multispectral-object-detection
  
#### Install requirements
 ```bash
$ pip install -r requirements.txt
```

## Dataset
-[HOD3K]  [download](http://shorturl.at/ahAY4) 

-[HSI-1]  [download](https://github.com/bupt-ai-cz/LLVIP)

-[VEDAI]  [download](https://downloads.greyc.fr/vedai/)


You need to convert all annotations to YOLOv5 format.

Refer: https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data

## Run
#### Download the pretrained weights
yolov5 weights (pre-train) 

-[yolov5s] [google drive](https://drive.google.com/file/d/1UGAsaOvV7jVrk0RvFVYL6Vq0K7NQLD8H/view?usp=sharing)

-[yolov5m] [google drive](https://drive.google.com/file/d/1qB7L2vtlGppGjHp5xpXCKw14YHhbV4s1/view?usp=sharing)

-[yolov5l] [google drive](https://drive.google.com/file/d/12OFGLF73CqTgOCMJAycZ8lB4eW19D0nb/view?usp=sharing)

-[yolov5x] [google drive](https://drive.google.com/file/d/1e9xiQImx84KFQ_a7XXpn608I3rhRmKEn/view?usp=sharing)



#### Change the data cfg
some example in data/multispectral/

#### Change the model cfg
some example in models/transformer/

note!!!   we used xxxx_transfomerx3_dataset.yaml in our paper.

### Train Test and Detect
train: ``` python train.py```

test: ``` python test.py```

detect: ``` python detect_twostream.py```


#### References

https://github.com/ultralytics/yolov5


