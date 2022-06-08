#################################################################### 
# Importing the important libraries
from distutils.errors import PreprocessError
import streamlit as st
from PIL import Image
import numpy as np
import time 
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from utlis import *
import sudukoSolver

#################################################################### 
# Setting the Height and Width.
heightImg = 450
widthImg = 450
# Importing Images using streamlit.
st.title("SUDOKU SOLVER")
st.subheader("SOLVE within seconds")
image = st.file_uploader("IMAGE PLEASE")

# Converting Image to JPEG image.



# Importing and Showing the Given Sudoku.
if image is not None:
    image = Image.open(image)
    # image = convertToJpeg(image)
    # st.image(image)
    image=np.array(image)
    try:
        st.subheader("Given Sudoku!")
        img = cv2.resize(image, (widthImg, heightImg))  # RESIZE IMAGE TO MAKE IT A SQUARE IMAGE
        st.image(img)
    except:
        st.subheader("Please upload a JPEG or JPG file.")
    
#####################################################################
# Importing the Prediction Model in model.
model = intializePredectionModel() 

########################################################################

try:    
    ########################################################################
    #### 1. Preparing the image for operations.
    img=image
    img = cv2.resize(img, (widthImg, heightImg))  # RESIZE IMAGE TO MAKE IT A SQUARE IMAGE
    imgBlank = np.zeros((heightImg, widthImg, 3), np.uint8)  # CREATE A BLANK IMAGE FOR TESTING DEBUGING IF REQUIRED
    imgThreshold=preProcess(img)
    
    
    # 2. Find all CONTOURS in image.
    imgContours = img.copy() # COPY IMAGE FOR DISPLAY PURPOSES
    imgBigContour = img.copy() # COPY IMAGE FOR DISPLAY PURPOSES
    contours, _ = cv2.findContours(imgThreshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # FIND ALL CONTOURS
    cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 3) # DRAW ALL DETECTED CONTOURS
    
    # Finding the biggest COUNTOUR and considering it SUDOKU
    biggest, maxArea = biggestContour(contours) # FIND THE BIGGEST CONTOUR
    
    
    if biggest.size != 0:
        biggest = reorder(biggest)
        cv2.drawContours(imgBigContour, biggest, -1, (0, 0, 255), 25) # DRAW THE BIGGEST CONTOUR
        pts1 = np.float32(biggest) # PREPARE POINTS FOR WARP
        pts2 = np.float32([[0, 0],[widthImg, 0], [0, heightImg],[widthImg, heightImg]]) # PREPARE POINTS FOR WARP
        
        # Straightning and streaching the SUDOKU table.
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
        
        imgDetectedDigits = imgBlank.copy()
        imgWarpColored = cv2.cvtColor(imgWarpColored,cv2.COLOR_BGR2GRAY)
    
        # Split the image in 81 small boxes and Find each available digit.
        imgSolvedDigits = imgBlank.copy()
        boxes = splitBoxes(imgWarpColored)
        
        numbers = getPredection(boxes, model)
        
        imgDetectedDigits = displayNumbers(imgDetectedDigits, numbers, color=(255, 0, 255))
        numbers = np.asarray(numbers)
        posArray = np.where(numbers > 0, 0, 1)
        
    
        # Find the solution of the Obtained borad, using backtracking algorithm.
        board = np.array_split(numbers,9)
        # print(board)
        try:
            sudukoSolver.solve(board)
        except:
            pass
        
        flatList = []
        for sublist in board:
            for item in sublist:
                flatList.append(item)
        solvedNumbers =flatList*posArray
        imgSolvedDigits= displayNumbers(imgSolvedDigits,solvedNumbers)
    
        # Printing the solution on the captured image.
        pts2 = np.float32(biggest) # PREPARE POINTS FOR WARP
        pts1 =  np.float32([[0, 0],[widthImg, 0], [0, heightImg],[widthImg, heightImg]]) # PREPARE POINTS FOR WARP
        matrix = cv2.getPerspectiveTransform(pts1, pts2)  # GER
        imgInvWarpColored = img.copy()
        
        imgInvWarpColored = cv2.warpPerspective(imgSolvedDigits, matrix, (widthImg, heightImg))
        
        inv_perspective = cv2.addWeighted(imgInvWarpColored, 1, img, 0.5, 1)
        
        # Printing the Solved SUDOKU with subheading
        st.subheader("Solution")
        st.image(inv_perspective)
    else:
        st.write("No Sudoku Found")
except:
    st.subheader("Please Upload an Image.")
