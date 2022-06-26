# Sudoku-Solver.
Solve your Sudoku, Just by scanning the image.

## Idea of the Project.
The idea of this project is inspired by a [problem on the Leetcode](https://leetcode.com/problems/sudoku-solver/) which solves the Sudoku. Solving the problem on leetcode, made me to think, Can I apply this algorithm to sovle the Sudoku directly from the image? As a result of that this project was made.

## Table of Content.
### Introduction.
### Technologies.
### Scope of functionality.
### Examples used.
### Project Status.
### Other Informations.
### Vote of Thanks.


## Introduction.
This project is intended to simplify the efforts made to solve the Sudoku. The project is coded in python using some common libraries, OpenCV, numpy. This project works in Five phases that are <strong> identify the Sudoku, extract the Sudoku, solve the sudoku, write the answer on the image inplace, and then return the image to the user </strong>.

### Identify the Sudoku.
To identify the Sudoku, we find the contours as well as their area in the image. The contour with the larget area, is being cosidered as the Sudoku Box. There is a scope of error if a bigger contour than Sudoku box is present in the image. In order to avoid confusion one should crop the image to have Sudoku box as the larget contour in the image.

### Extract the Sudoku.
In order to extract the Sudoku we are dividing the identified Sudoku in 9 vertical as well as 9 horizontal equal parts. These 81 images are than passed through a pretrained model on MNIST dataset to recognize which digit is present in the box. We have set a threshold of 80% accuracy if a model can identify the digit with more than 80% accuracy than we will fill the position in array with that number, else the box will be considered as empty and 0 will be filled at that position. We will follow this process for all 81 boxes and make the 2-D array of Sudoku.

### Solve the Sudoku.
After extraction of the sudoku, we will solve the sudoku using the backtracking considering the 0 as the empty position. Using backtracking we will find the solution to the Sudoku, in a separate 2-D Matrix.

### Writing the Solution to the Image.
After solving the Sudoku we will write the solution on the image, it is the most tricky work since it take a lot of hit and trial to find the optimal position to place the digits on the image.

### Returning the image to the user.
After performing the above steps we will return the image to the user where the black postions of the Sudoku will be filled with the answers.
<br>
#### Example
<img src="https://github.com/shubhammishra115/Sudoku-Solver/blob/main/Example/1.jpg" height="450">
<br>

## Technologies used.
The following technologies are used in the Project.
### Computer Vision and Image Processing
Computer Vision is the soul part of the project as it takes input as an image. Once we have the input image we Process the image to extract the sudoku board from the image and create a Sudoku matrix.

### Classification.
The Sudoku Solver is also a classification based problem as we have to classify the numbers present in each box of the Sudoku. The classification model is trained on MNIST dataset.

### Deep Learning.
Deep Learning is a machine learning technique which involves the use of Neural Networks. 

#### Convolution Neural Networks.
We have trained our model on MNIST dataset using the CNN (Convolutional Neural Networks).

## Scope of Functionality.
The Sudoku Solver works fine for the images uploaded in JPEG format provided the quality of image is good.

### Where Project fails or Prompts an error.
#### Quality of the image is poor.
If the quality of the image is poor then it will be difficult for the machine to interpret and extract the sudoku.

#### Sudoku is enclosed in some rectangle.
Since we have assumed that the largest contour is the Sudoku, if there will be a contour that is even larger than the Sudoku, then the model will miss interpret the Sudoku and will provide the wrong output. <br>
#### Example:<br>
<img src="https://github.com/shubhammishra115/Sudoku-Solver/blob/main/Example/wrong%20example.jpg" width="450">
<br>

The model will not perform optimally for the above provided image and will provide wrong answer.

## Examples Used
As an example we have used three images.
<br>
<h4> Example 1. </h4>
<img src="https://github.com/shubhammishra115/Sudoku-Solver/blob/main/Example/1.jpg" height="450">
<br>
<h4> Example 2. </h4>
<img src="https://github.com/shubhammishra115/Sudoku-Solver/blob/main/Example/2.jpg" height="450">
<br>
<h4> Example 3. </h4>
<img src="https://github.com/shubhammishra115/Sudoku-Solver/blob/main/Example/3.jpg" height="450">
<br>

## Project Status
Project will be updated to add new features or if some bug will be encountered.

## Other Information
Language Used: Python. <br>
Library Used: Numpy, cv2, keras, streamlit, BytesIO, PIL. <br>
Technology Used: Image Processing, Machine Learning, Deep Learing, Convolutional Neural Network, Classification.

## Vote of Thanks
This Project was not possible without the help and support of [Mohammad Asad](https://www.linkedin.com/in/mohammad-asad-a50534190/), SDE-I at Amazon.
