from calendar import day_abbr
import rtree
import matplotlib.pyplot as plt
import numpy as np
import os
import random
import time

pickle_in = open("dict.pickle","rb")
data_vec=pickle.load(pickle_in)

prop = rtree.index.Property()
prop.dimension = 128
prop.buffering_capacity = 3
prop.dat_extension = "data"
prop.idx_extension = "index"

if os.path.exists("puntos.data"): os.remove("puntos.data")
if os.path.exists("puntos.index"): os.remove("puntos.index")

var=0

for i in data_vec:
    ind = rtree.index.Index("puntos", properties = prop)
    ind.insert(var, data_vec[i])
    var=var+1
