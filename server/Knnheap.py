import pickle
import os
import face_recognition
import numpy as np
import heapq

pickle_in = open("dict.pickle","rb")
data_vec=pickle.load(pickle_in)

route="./IMG_4300mod.jpg"
encoding = face_recognition.face_encodings(face_recognition.load_image_file(route))[0]

def KnnHeap(Query,k,data):
    result=[]
    for i in data:
        for j in data[i]:
            dist=face_recognition.face_distance([Query],j)[0]
            heapq.heappush(result,(dist,i))
    return list(heapq.heappop(result) for i in range(k))

def RangeSearch(Query,range,data):
    result=[]
    for i in data:
        for j in data[i]:
            dist=face_recognition.face_distance([Query],j)[0]
            if(dist<range): result.append(i)
    return result


print(KnnHeap(encoding,10,data_vec))
#print(RangeSearch(encoding,2,data_vec))
