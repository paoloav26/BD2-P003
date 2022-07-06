import pickle
import os
import face_recognition
import numpy as np

pickle_in = open("dict.pickle","rb")
data_vec=pickle.load(pickle_in)

print(data_vec)
route="./IMG_4300mod.jpg"
encoding = face_recognition.face_encodings(face_recognition.load_image_file(route))[0]
print(encoding)

min=1000000
name=""
for i in data_vec:
    for j in data_vec[i]:
        if min > face_recognition.face_distance([encoding],j)[0]:
            min=face_recognition.face_distance([encoding],j)[0]
            name=i
    
print(min,name)