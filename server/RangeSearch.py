import pickle
import os
import face_recognition
import numpy as np
import heapq

pickle_in = open("dict.pickle","rb")
data_vec=pickle.load(pickle_in)
pickle_in.close()

route="./briney.jpg"
encoding = face_recognition.face_encodings(face_recognition.load_image_file(route))[0]

def RangeSearch(Query,range,data):
    result=[]
    for i in data:
        for j in data[i]:
            dist=face_recognition.face_distance([Query],j)[0]
            if(dist<range): result.append(i)
    return result

print(set(RangeSearch(encoding,0.6,data_vec)))