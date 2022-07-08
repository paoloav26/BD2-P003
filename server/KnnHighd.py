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

    vectores_caracteristicos_np=np.array([i[0][0] for i in vectores_caracteristicos]).astype('float32')

    nombres=[]
    index=faiss.read_index("./server/hnsw.faiss")
    result=index.search(np.array([Query]).astype('float32'),k=k)
    for j in range(k):
        nombres.append((result[0][0][j],vectores_caracteristicos[result[1][0][j]][0][1]))

    return(nombres)

#route="./briney.jpg"
#encoding = face_recognition.face_encodings(face_recognition.load_image_file(route))[0]
#
#pickle_in = open("dict.pickle","rb")
#data_vec=pickle.load(pickle_in)
#pickle_in.close()
#
#print(KnnHighD(encoding,10,data_vec))