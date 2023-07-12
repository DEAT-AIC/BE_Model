from flask import Flask, make_response, request, jsonify, render_template, abort
import os
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv

load_dotenv()


os.putenv("LANG", "en_US.UTF-8")
os.putenv("LC_ALL", "en_US.UTF-8")

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        # self.classifier = predict(self.filename)


@app.route("/", methods=["GET"])
@cross_origin()
def home():
    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    clApp = ClientApp()
    # app.debug = True
    app.run(host="0.0.0.0", port=port)
