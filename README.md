# Sudoku-Solver
Solve you Sudoku, Just by scanning the image.

#### Idea 
The idea of this project is inspired by a problem on the Leetcode which solves the Sudoku, in order to make something unique this 

## Table of Content.
### Introduction.
### Technologies.
### Scope of functionality.
### Examples used.
### Project Status.
### Other Informations.


## Introduction
This project is intended to simplify the efforts made to solve the Sudoku. The project is coded in python using some common libraries, OpenCV, numpy. This project works in Five phases that are identify the Sudoku, extract the Sudoku, solve the sudoku, write the answer on the image inplace, and then return the image to the user.

### Identify the Sudoku.
To Identify the Sudoku, we find the contours in the images, and find the area of the contours. The contour with the larget area, is being cosidered as the Sudoku Box. There is a scope of error if a big contour than Sudoku box is present in the image. In order to avoid confusion one should crop the image to have Sudoku box as the larget contour in the image.

### Extract the Sudoku.
In order to extract the Sudoku we are dividing the identified Sudoku in 9 vertical as well as 9 horizontal equal parts. These 81 images are than passed through a pretrained model on MNIST dataset to recognize which digit is present in the box, we have used a threshold of 80% accuracy if a model can identify the digit with more than 80% than we will fill the array with that number, else the box will be considered as empty and 0 will be filled at that place. We will follow this process for all 81 boxes and make the 2-D array of Sudoku.

### Solve the Sudoku.
After extraction of the sudoku, we will solve the sudoku using the backtracking considering the 0 as the null position. Using backtracking we will find the solution in a matrix.

### Writing the Solution to the Image 
After solving the Sudoku we will write the image on the image, it is the most tricky work since it take a lot of hit and trial to find the optimal position of place the digits on the image.

### Returning the image to the user.
After performing the above steps we will return the image to the user where the image will be as it is, with answers flled on the blank spaces.

## Technologies used.
