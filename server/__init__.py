from flask import (
    abort, 
    jsonify,
    Flask, 
    request,
    render_template
)
import os
from Knnheap import KnnHeap
from KnnHighd import KnnHighD
from KNNRtree import KnnRtreee
import face_recognition
import pickle
import time


def create_app(test_config=None):
    app=Flask(__name__)
    app.config["IMAGE_UPLOADS"] = r"./server/static"

    # endpoints
    @app.route('/',methods=['GET','POST'])
    def home():
        
        KNNheap=[]
        KNNHighd=[]
        KNNRtree=[]
        error_msg=""

        if request.method == "POST":

            if request.files:
                error_msg=""
                image = request.files["image"]
                k = int(request.form.get("knumber"))

                image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

                route="./server/static/"+image.filename
                try:
                    encoding = face_recognition.face_encodings(face_recognition.load_image_file(route))[0]

                    pickle_in = open("./server/dict.pickle","rb")
                    data=pickle.load(pickle_in)
                    pickle_in.close()

                    image_photo="./static/"+image.filename
                    
                    start_time = time.time()
                    KNNheap=KnnHeap(encoding,k,data)
                    KNNheap_time = round(time.time() - start_time,8)

                    start_time = time.time()
                    KNNHighd=KnnHighD(encoding,k,data)
                    KNNHighd_time = round(time.time() - start_time,8)

                    start_time = time.time()
                    KNNRtree=KnnRtreee(encoding,k,data)
                    KnnRtreee_time = round(time.time() - start_time,8)

                except Exception as e:
                    print(e)
                    error_msg="ERROR: Esa imagen no puede ser procesada"

            return render_template("index.html",
            error_msg=error_msg,
            input_photo=image_photo,
            Knnheap=KNNheap,
            KNNheap_time=KNNheap_time,
            KnnHighD=KNNHighd,
            KNNHighd_time = KNNHighd_time,
            KnnR=KNNRtree,
            KnnRtreee_time=KnnRtreee_time)

            
        return render_template("index.html")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
