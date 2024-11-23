# Use a Pre-trained Image Classifier to Identify Dog Breeds

This project is part of Udacity's 'AI Programming with Python' Nanodegree. 

Here, I used a created image classifier to identify dog breeds. The project utilizes pre-trained convolutional neural network (CNN) models to classify images of dogs and identify their breeds. By leveraging powerful models such as VGG, AlexNet, and ResNet, the classifier processes images from a specified directory and returns predictions along with accuracy metrics. This tool is beneficial for dog enthusiasts, researchers, and anyone interested in animal classification.

## Table of Contents 
1. [Installation Instructions](#installation-instructions) 
2. [Usage](#usage) 
3. [Features](#features) 
4. [License](#license) 
6. [Acknowledgments](#acknowledgments) 


## Installation Instructions

1. Clone the repository:

```bash
git clone https://github.com/aakanksha-singh-hub/dog-breed-classifier.git 
```

2. Navigate to the project directory:

```bash
cd dog-breed-classifier
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the image classifier, use the following command:
```bash
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
```
-   `--dir`: Specify the directory containing pet images (default is  `pet_images/`).
-   `--arch`: Choose the model architecture (default is  `vgg`).
-   `--dogfile`: Provide the file containing dog names (default is  `dognames.txt`)

## Features

-   Classifies images of dogs into various breeds using pre-trained models (VGG, AlexNet, ResNet).
-   Provides accuracy metrics for each model, including the percentage of correct classifications.
-   Supports command-line arguments for flexibility in input directories and model selection.
-   Displays detailed results, including incorrect classifications and total elapsed runtime.



## License

This project is licensed under the MIT License. [MIT](https://choosealicense.com/licenses/mit/)


## Acknowledgments

- Thanks to the creators of the pre-trained models used in this project.
- Special thanks to the Udacity community for their support and resources.

