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
import face_recognition
import pickle


def create_app(test_config=None):
    app=Flask(__name__)
    app.config["IMAGE_UPLOADS"] = r"./server/static"

    # endpoints
    @app.route('/',methods=['GET','POST'])
    def home():
        
        KNNheap=[]
        KNNHighd=[]
        error_msg=""

        if request.method == "POST":

            if request.files:
                error_msg=""
                image = request.files["image"]

                image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

                route="./server/static/"+image.filename
                try:
                    encoding = face_recognition.face_encodings(face_recognition.load_image_file(route))[0]

                    pickle_in = open("./server/dict.pickle","rb")
                    data=pickle.load(pickle_in)
                    pickle_in.close()

                    image_photo="./static/"+image.filename
                    KNNheap=KnnHeap(encoding,5,data)
                    KNNHighd=KnnHighD(encoding,5,data)
                    
                except Exception as e:
                    print(e)
                    error_msg="ERROR: Esa imagen no puede ser procesada"

            return render_template("index.html",error_msg=error_msg,input_photo=image_photo,Knnheap=KNNheap,KnnHighD=KNNHighd)

            
        return render_template("index.html")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)