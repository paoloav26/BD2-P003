import faiss
import numpy as np
import face_recognition
import pickle

#route="./briney.jpg"
#encoding = face_recognition.face_encodings(face_recognition.load_image_file(route))[0]


def KnnHighD(Query,k,data):

    vectores_caracteristicos=[]

    for nombre_persona in data:
        for vector_caracteristico in data[nombre_persona]:
            vectores_caracteristicos.append((vector_caracteristico,nombre_persona))

    vectores_caracteristicos_np=np.array([i[0] for i in vectores_caracteristicos]).astype('float32')

    nombres=[]
    index=faiss.read_index("./server/hnsw.faiss")
    for i in index.search(np.array([Query]).astype('float32'),k=k)[1]:
        for j in i:
            nombres.append(vectores_caracteristicos[j][1])

    return(nombres)

#route="./briney.jpg"
#encoding = face_recognition.face_encodings(face_recognition.load_image_file(route))[0]
#
#pickle_in = open("dict.pickle","rb")
#data_vec=pickle.load(pickle_in)
#pickle_in.close()
#
#print(KnnHighD(encoding,10,data_vec))