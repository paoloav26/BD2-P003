from calendar import day_abbr
import rtree
import matplotlib.pyplot as plt
import numpy as np
import os
import random
import time
import pickle

prop = rtree.index.Property() 
prop.dimension = 128
prop.buffering_capacity = 3
prop.dat_extension = "data"
prop.idx_extension = "index"

def crear():
    pickle_in = open("dict.pickle","rb")
    data_vec=pickle.load(pickle_in)


    if os.path.exists("puntos.data"): os.remove("puntos.data")
    if os.path.exists("puntos.index"): os.remove("puntos.index")

    ind = rtree.index.Index("puntos", properties = prop)

    var=0
    
    for i in data_vec:
        ind.insert(var, data_vec[i][0][0])
        var=var+1

def KnnRtreee(Query,k,data):
    ind = rtree.index.Index("./server/puntos", properties = prop)

    pickle_in = open("./server/dict_mapeo.pickle","rb")
    mapeo=pickle.load(pickle_in)
    res=ind.nearest(Query, num_results=k)
    arr=[]
    for i in list(res):
        arr.append(mapeo[i])

    return arr

#crear()


