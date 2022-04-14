# Transformer Show Attend And Tell
This repository contains an adaptation of the architecture proposed by the [Show, Attend and Tell](https://arxiv.org/pdf/1502.03044.pdf) paper. Our proposal focuses on replacing the convolutional component used by its original encoder by a structure based on Transformer networks. This contribution was respectively documented in the paper [Deep Learning Approaches Based on Transformer Architectures for Image Captioning Tasks](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9739703).

## Description of the main files

- train.py: 
- caption.py:
- models.py:

## Dataset

The 2014 version of the COCO dataset was used for this work. The [Training](http://images.cocodataset.org/zips/train2014.zip) and [Validation](http://images.cocodataset.org/zips/val2014.zip) sets can be found in the attached links.

Once the dataset has been downloaded, a preliminary step must be carried out before it can be used. Due to the considerable number of images, the project works with HDF5 files where all images will be split and stored, while JSON files will include the associated captions and caption lengths. To do this, it is required to run the script **create_input_files.py**. This file makes use of the function of the same name within the **utils.py** file, which specifies the nature of each field that the user must edit depending on its directory structure.

## Relevant commands
- Training of the network:
python train.py
- Inference for a specific input image: python caption.py --img='path/to/image.jpeg' --model='path/to/BEST_checkpoint_coco_5_cap_per_img_5_min_word_freq.pth.tar' --word_map='path/to/WORDMAP_coco_5_cap_per_img_5_min_word_freq.json'

## Credits
This work was inspired by and based on the implementation proposed in this [repository](https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Image-Captioning#implementation).
