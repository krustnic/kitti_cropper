# KITTI_CROPPER

Python script for croping images based on KITTI file format:

```
Car 0.00 0 0.0 470.00 199.00 877.00 414.00 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
```

Can be useful if you want to use your annotated images for NN classification task

## Usage

```
python kitti_cropper samples
```

`samples` folder should be with the following structure:

```
- samples
|- 1.jpg
|- 1.txt # KITTI file
|- 2.jpg
|- 2.txt
```

Image files should be with one of the following extension: "jpg", "jpeg", "png".
Output folder structure would be:

```
- samples
|- Car // folder with cropped images by "Car" class ([source image name]-[index].[source extension])
|-- 1-1.jpg
|-- 1-2.jpg
|-- 2-1.jpg
|-- 2-2.jpg
|- Human
|-- 1-1.jpg
|-- 2-1.jpg
|- 1.jpg
|- 1.txt
|- 2.jpg
|- 2.txt
```