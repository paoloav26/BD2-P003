import pickle
import os
import face_recognition
import numpy as np

PATH = './lfw/'

pickle_out = open("dict.pickle","wb")

file_dir = []
for root,d_names,f_names in os.walk(PATH):
    for f in f_names:
        file_dir.append((root[6:],root+'/'+f))

dict_name_encodings_arr = {}
for person_name,route in file_dir:
    if person_name not in dict_name_encodings_arr:
        try:
            dict_name_encodings_arr[person_name] = [face_recognition.face_encodings(face_recognition.load_image_file(route))[0]]
        except:
            continue
    else:
        try:
            dict_name_encodings_arr[person_name].append(face_recognition.face_encodings(face_recognition.load_image_file(route))[0])
        except:
            continue


pickle.dump(dict_name_encodings_arr,pickle_out)
pickle_out.close()

pickle_in = open("dict.pickle","rb")
data_vec=pickle.load(pickle_in)

#print(data_vec)