# FuQdan: Quantum Image Classification for Alzheimer's Detection (Team 12)

## What is this about
FuQdan is a quantum computing algorithm that acts as a binary classifier for MRI scan images. The goal of this project is to classify MRI scan images as with dementia or no dementia. By leveraging the power of quantum computing, we aim to provide a more efficient method for analyzing MRI scans in terms of space complexity.

We use the FRQI algorithm to represent an MRI scan image into quantum states and calculate a reference image of a scan with dementia. The reference image is derived from the mean of multiple images. Test images are compared against this reference image using a quantum algorithm that converts the image to quantum states via FRQI. We then calculate the fidelity between the reference image and a test image, convert this fidelity to euclidean distance, and classify the image based on a threshold.

## How to use
Obtain MRI images from the Alzheimer's Dataset available at https://www.kaggle.com/datasets/tourist55/alzheimers-dataset-4-class-of-images

Run the `get_theta_rep.ipynb` notebook to preprocess the grayscale image into vectors of theta values.
Run the `Quantum_Image_Classification.ipynb` notebook, which contains the algorithm that measures the similarity of an image with the reference image.
The output will be the likelihood of Alzheimer's disease in the test images.

## Notebooks
`get_theta_rep.ipynb` - This notebook contains the preprocessing of the grayscale image to vectors of theta values.

`Quantum_Image_Classification.ipynb` - This notebook contains the main quantum algorithm for measuring the similarity between an image and the reference image.

## Data
Dataset: Alzheimer's Dataset from Kaggle - https://www.kaggle.com/datasets/tourist55/alzheimers-dataset-4-class-of-images

`sample_data` folder: Contains sample MRI images for testing the algorithm.

`Preprocessed_Dataset` folder: Contains examples of the dataset preprocessed to be vectors of theta values, which then get encoded into quantum states by our quantum algorithm.

## Business Value
FuQdan provides an efficient approach to MRI scan analysis in terms of space complexity. Comparing our quantum computing algorithm with classical methods, we find that both have O(n) time complexity, where n is the number of pixels in an image. However, our quantum method has a space complexity of O(log_2 n) compared to O(n) in comparable classical methods, resulting in lower memory requirements. This can be valuable in healthcare settings, where efficient resource management and accurate diagnosis are essential.

This project is the output of a 3-day hackathon organized by NYU Abu Dhabi, running from April 28 to 30, 2023.