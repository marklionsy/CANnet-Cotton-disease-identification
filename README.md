# CANnet🌻Cotton disease identification🌱
``CANnet`` utilizes artificial intelligence technology to assist agricultural producers in achieving intelligent identification of crop diseases. ``CANnet`` reduces the input of labor costs and has better accuracy and higher recognition efficiency compared to manual recognition.
![](/fig/cotton_1.png "cotton")

## Dataset
Changji Hui Autonomous Prefecture, Xinjiang, China (``self collected``)<br>
![](/fig/cotton.png "cotton_dataset")
If you would like to use this dataset for academic research, you can contact: 107552204060@stu.xju.edu.cn<br>
********************************************************
## Experimental effect🎄
| Model | cotton | cucumber |  
| :--- | :---: | ---: |  
| aaaaa | bbbbb | ccccc |  
| aa | bb | cc | 

********************************************************
## Train🍉
You can train the model using the following commands:<br>
CPU:<br>
python Model/train.py configs/resnet/resnet18_8xb32_in1k.py --work-dir resnet18_dir/root<br>
GPU:<br>
CUDA_VISIBLE_DEVICES=7 python Model/train.py configs/resnet/resnet18_8xb32_in1k.py --work-dir resnet18_dir/root<br>
********************************************************
## Test🍒
1.You can test it using the following code:<br>
CPU :<br>
python  Model/test.py  configs/resnet/resnet18_8xb32_in1k.py``Your test parameter file``  cotton/best_accuracy_top1_epoch_xx.pth``Model weight file``<br>
GPU :<br>
CUDA_VISIBLE_DEVICES=0``GPU``  python Model/test.py configs/resnet/resnet18_8xb32_in1k.py``Your test parameter file``  cotton/best_accuracy_top1_epoch_xx.pth``Model weight file``<br>

2.You can also directly use our trained weight file to test the dataset, and download the weight file through the following methods:<br>
Link：https://pan.baidu.com/s/1lPRjAdVsgG_pLbx6Aynppw  password：1998
********************************************************
## Acknowledgments🍆
``Model/CAN-Net.py`` is the code for the feature extraction section, while ``cls_head/ln_head.py`` is the code for the classification header section.
This project is in ``MMPretrain（ https://github.com/open-mmlab/mmpretrain ）``Conduct experiments within the framework
