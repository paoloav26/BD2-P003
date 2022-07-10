import pickle
import os
import face_recognition
import numpy as np

PATH = './static/lfw/'

pickle_out = open("dict_mapeo.pickle","wb")

file_dir = []
ans={}
var=0
for root,d_names,f_names in os.walk(PATH):
    for f in f_names:
        ans[var]=root+'/'+f
        var=var+1

pickle.dump(ans,pickle_out)
pickle_out.close()
