import tkinter
import numpy as np
from PIL import Image, ImageTk
import cv2 
import os
import random 
import tensorflow as tf
from tensorflow.keras.models import load_model
from keras.preprocessing import image

#load the pretrained model
model = load_model('RPS_detectionModel_v4.h5')
# v4 size(100,100), v5 size(224,224)
width = 100
height = 100

start_point = (300, 150)
end_point = (500, 380)  
# image_scissor_path = 'sample_scissor.png'
# image_scissor_path = 'sample_rock.png'
# image_scissor_path = 'sample_paper.png'
image_mickey_path = 'sample.png'
sample_images_path= "sample_images"
files=os.listdir(sample_images_path)

# dim = (400,500)
# img_ai_read = Image.open(image_mickey_path)
# img_ai_read = img_ai_read.resize(dim) 

dim = (400,500)
randomly_selected = Image.open(image_mickey_path)
randomly_selected = randomly_selected.resize(dim)

window=tkinter.Tk()
window.title("Rock Paper Scissors")
window.configure(background='white')


frame=np.random.randint(0,255,[100,100,3],dtype='uint8')

player_box1 = tkinter.Label(window) #,image=img)
player_box1.grid(row=0,column=0,columnspan=3,pady=1,padx=10)

player_box2=tkinter.Label(window) #,image=img)
player_box2.grid(row=0,column=4,columnspan=3,pady=1,padx=100)
player_box2.configure(background='white')

message="Player"
player_text=tkinter.Label(window,text=message)
player_text.grid(row=1,column=1,pady=1,padx=10)
player_text.configure(font=('Calibri', 25))
player_text.configure(background='white')


message="Mickey"
mickey_text=tkinter.Label(window,text=message)
mickey_text.grid(row=1,column=5,pady=1,padx=10)
mickey_text.configure(font=('Calibri', 25))
mickey_text.configure(background='white')

 
message=""
mickey_counter=tkinter.Label(window,text=message)
mickey_counter.grid(row=2,column=5,pady=1,padx=1)
mickey_counter.configure(background='white')
mickey_counter.configure(font=('Calibri', 24))

message=""
player_counter=tkinter.Label(window,text=message)
player_counter.grid(row=2,column=1,pady=1,padx=10)
player_counter.configure(background='white')
player_counter.configure(font=('Calibri', 24))

gif_label = tkinter.Label(window,image="")
gif_label.grid(row=1,column=2,pady=1,padx=10,columnspan=3)
gif_label.configure(background='white')
# gif_label.pack()  

message="------Score------"
score_text=tkinter.Label(window,text=message)
score_text.grid(row=2,column=3,pady=1,padx=10) 
score_text.configure(background='white')
score_text.configure(font=('Calibri', 20))

cam = 1

### for animation

gif_file="countdown.gif"

info = Image.open(gif_file)

anim_frames = info.n_frames  # gives total number of frames that gif contains

# creating list of PhotoImage objects for each frames
anim_im = [tkinter.PhotoImage(file=gif_file,format=f"gif -index {i}") for i in range(anim_frames)]

anim_count = 0
anim = None

### score counter 
player_score = 0
mickey_score = 0


def video_capture():
    global frame
    global cam
    global randomly_selected
    cam = cv2.VideoCapture(0)
    #cv2.namedWindow("Experience_in_AI camera")
    while True:
        # key = cv2.waitKey(1) & 0xFF
        ret, frame = cam.read()
        frame = cv2.flip(frame, 1)
       
        cv2.rectangle(frame, start_point, end_point, (0, 255, 0), 2)
        
        #Update the image to tkinter...
        frame_=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        img_update = ImageTk.PhotoImage(Image.fromarray(frame_))
        player_box1.configure(image=img_update)
        player_box1.image=img_update
        player_box1.update()
        
        img_ai = ImageTk.PhotoImage(randomly_selected)
        player_box2.configure(image=img_ai)
        player_box2.image=img_ai
        player_box2.update()

        if not ret:
            print("failed to grab frame")
            break

def player_choice_predict():
    crop_img = frame[start_point[1]:end_point[1], start_point[0]:end_point[0]]
    # cv2.imshow("crop_img", crop_img)
    dim_img = (width, height)
    # resize image
    crop_img = cv2.resize(crop_img, dim_img, interpolation = cv2.INTER_AREA)
    im = Image.fromarray(crop_img, 'RGB')
    img_array = np.array(im)
    img_array = np.expand_dims(img_array, axis=0)
    # # Use the model to predict
    pred = model.predict(img_array)
    
    dict_key = pred.argmax()
    label_dict = {0: 'paper', 1: 'rock', 2: 'scissor'}
    pred_label = label_dict[dict_key]
    player_text.configure(text = pred_label)
    
    
    return pred_label

def mickey_choice():  
    global randomly_selected
    global mickey_score
    randomly_selected_path = random.choice(files) 
    dim = (400,500)
    randomly_selected = Image.open(sample_images_path+'/'+randomly_selected_path)
    randomly_selected = randomly_selected.resize(dim)
    img_ai = ImageTk.PhotoImage(randomly_selected)
    player_box2.configure(image=img_ai)
    player_box2.image=img_ai
    player_box2.update()
    randomly_selected_rps_name = randomly_selected_path.strip(".png").split('_')[1]
    mickey_text.configure(text=randomly_selected_rps_name)
   
    
    return randomly_selected_rps_name
    
    # global cam
    # cam.release()
    # cv2.destroyAllWindows()
    # print("Stopped!")
    
def animation(count):
    global anim_im
    global player_score
    global mickey_score
    if count < anim_frames:
        im2 = anim_im[count]

        gif_label.configure(image=im2)
        count += 1
             
        anim = window.after(180,lambda :animation(count))
    else:
        p_opt = player_choice_predict()
        m_opt = mickey_choice()
        
        if p_opt == 'rock' and m_opt == 'scissor':
            player_score += 1
        elif p_opt == 'rock' and m_opt == 'paper':
            mickey_score +=1
        elif p_opt == 'paper' and m_opt == 'rock':
            player_score += 1
        elif p_opt == 'paper' and m_opt == 'scissor':
            mickey_score +=1
        elif p_opt == 'scissor' and m_opt == 'paper':
            player_score += 1
        elif p_opt == 'scissor' and m_opt == 'rock':
            mickey_score +=1
        
        player_counter.configure(text = player_score)
        mickey_counter.configure(text = mickey_score)
        

button1_height = 6
button1 = tkinter.Button(window,text="Start",command=video_capture,height=5,width=20)
button1.grid(row=1,column=0,pady=10,padx=10)
button1.config(height=1*button1_height,width=20)
button1.configure(font=('Calibri', 14))
button1.configure(background='green')


button2_height = 6
# button2 = tkinter.Button(window,text="Stop",command=video_capture_end,height=5,width=20)
button2 = tkinter.Button(window,text="Shoot !!!",command=lambda :animation(anim_count),height=5,width=20)
button2.grid(row=1,column=6,pady=10,padx=10)
button2.config(height=1*button1_height,width=20)
button2.configure(font=('Calibri', 14))
button2.configure(background='red')


window.mainloop()

cam.release()
cv2.destroyAllWindows()