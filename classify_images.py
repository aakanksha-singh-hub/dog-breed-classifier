#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from classifier import classifier

def classify_images(images_dir, results_dic, model):
    """
    Classifies images using the specified CNN model and updates results_dic with classifier labels and match info.
    Parameters:
      images_dir - Path to the folder of images to classify (string)
      results_dic - Dictionary with image filename as key and list as value. List index 0 = true label (string).
      model - CNN model architecture to use: 'resnet', 'alexnet', or 'vgg' (string)
    Returns:
      None (results_dic is updated in place)
    """
    for key in results_dic:
        image_path = images_dir + '/' + key
        model_label = classifier(image_path, model)
        model_label = model_label.lower().strip()
        truth = results_dic[key][0]
        if truth in model_label:
            results_dic[key].extend([model_label, 1])
        else:
            results_dic[key].extend([model_label, 0])

