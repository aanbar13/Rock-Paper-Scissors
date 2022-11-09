# Rock-Paper-Scissors
This project is a fun game that can be played with a bot which randomly shoots either rock or paper or scissors. Computer vision techniques are used to capture the hand gesture of the player via webcam which then is predicted by a trained machine learning model to be one of the mentioned three options.<br> 
# Training Data  
For training the model for the project, the dataset that was used can be found here - https://www.kaggle.com/datasets/drgfreeman/rockpaperscissors. The dataset contains a total of 2188 RGB images (300 x 200) labeled as paper (712 images), rock (726 images) and scissors (750 images).<br>  
# Summary of the work 
Methodology of the project in brief -<br>
•	API used for building and training the model was Keras<br>
•	Data augmentation (horizontal and vertical flip, width and height shift, shear) was performed to pre-process data<br>
•	20% data from the mentioned dataset was taken as test data<br>
•	ResNet50 architecture was used for training the model<br> 
•	Validation accuracy obtained was approximately 99%<br> 
•	OpenCV was used for taking in real-time hand gestures of the player<br>
# Performance 
![Training Performace](Performance.PNG) 
# Let's Play! 
For model development and performance, check the provided ResNet50_rock_paper_scissors_v4.ipynb file. Run the GUI_Rock_paper_scissor_final.py file with a functioning webcam plugged in. In the game window popped up, ‘Start’ button will start taking live feed and ‘Shoot’ button will make the bot play. To make sure the prediction from the live feed is as mentioned, noiseless/ monochrome background is a pre-requisite.<br>

