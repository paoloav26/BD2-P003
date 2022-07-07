import pickle
from turtle import pen
import faiss
import numpy as np
import face_recognition

pickle_in = open("dict.pickle","rb")
data_vec=pickle.load(pickle_in)
pickle_in.close()

d = 128
M = 12

index = faiss.IndexHNSWFlat(d,M)

vectores_caracteristicos=[]

for nombre_persona in data_vec:
    for vector_caracteristico in data_vec[nombre_persona]:
        vectores_caracteristicos.append((vector_caracteristico,nombre_persona))

vectores_caracteristicos_np=np.array([i[0] for i in vectores_caracteristicos]).astype('float32')

#Construccion del HNWS
index.add(vectores_caracteristicos_np)

route="./briney.jpg"
encoding = face_recognition.face_encodings(face_recognition.load_image_file(route))[0]

vectores_caracteristicos_a_buscar=[]

nombres=[]
for i in index.search(np.array([encoding]).astype('float32'),k=4)[1]:
    for j in i:
        nombres.append(vectores_caracteristicos[j][1])

print(nombres)