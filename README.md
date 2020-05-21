# Helmet_Image_Classifier
This project contains Helmet, Non-Helmet Image classifier using LeNet.

### Download Custom dataset from below URL

```
https://drive.google.com/drive/folders/1CQIXgT-qqD6EWLDbTkZqaYEVT4AOnHmF?usp=sharing
```
Dataset contain the helmet and non-helmet images from customally collected from goggle.

### Install Pre-requiest
```
pip install -r requirement.txt
```

## Train Model
```
python train_network.py --dataset dataset --model helmet_not_helmet.model
```

## Test Model
```
python predict.py --model helmet_not_helmet.model --image test_images/1_1.jpg
```

#### Reference:
https://www.pyimagesearch.com/2017/12/11/image-classification-with-keras-and-deep-learning/
