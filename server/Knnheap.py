import pickle
import os
import face_recognition
import numpy as np
import heapq

pickle_in = open("dict.pickle","rb")
data_vec=pickle.load(pickle_in)

print(data_vec)
route="./IMG_4300mod.jpg"
encoding = face_recognition.face_encodings(face_recognition.load_image_file(route))[0]
print(encoding)

def KnnHeap(Query,k,data):
    result=[]
    for i in data_vec:
        for j in data_vec[i]:
            dist=face_recognition.face_distance([Query],j)[0]
            heapq.heappush(result,(dist,i))
    return list(heapq.heappop(result) for i in range(k))

print(KnnHeap(encoding,10,data_vec))