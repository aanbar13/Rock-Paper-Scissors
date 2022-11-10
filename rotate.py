# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 16:47:23 2022

@author: USER
"""
# Importing the libraries
from PIL import Image
import glob
from tqdm import tqdm

path = "Rock-Paper-Scissors-2/scissors/*"

path_list = glob.glob(path)


for p in tqdm(path_list):
    im = Image.open(p)
    im=im.rotate(270, expand=True)
    # im.show()
    im.save(p)
