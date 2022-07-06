from crypt import methods
from flask import (
    abort, 
    jsonify,
    Flask, 
    request,
    render_template
)


def create_app(test_config=None):
    app=Flask(__name__)

    # endpoints
    @app.route('/',methods=['GET'])
    def home():
        return render_template("index.html")

    @app.route('/',methods=['POST'])
    def home_post():
        return render_template("index.html")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)