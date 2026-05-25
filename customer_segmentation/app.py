from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np

from kmeans_model import predict_cluster

app = Flask(__name__)

# mengizinkan frontend request ke flask
CORS(app)

# load centroid hasil training
centroids = np.load("./data/centroids.npy")

# label cluster
label_map = {
    0: "Low Income",
    1: "Middle Income",
    2: "High Income"
}


@app.route("/")
def home():

    return jsonify({
        "message": "Customer Segmentation API"
    })


@app.route("/predict", methods=["POST"])
def predict():

    try:

        # ambil request json
        data = request.get_json()

        umur = data["umur"]
        penghasilan = data["penghasilan"]

        # data customer baru
        data_baru = [umur, penghasilan]

        # predict cluster
        cluster = predict_cluster(data_baru, centroids)

        # hasil response
        hasil = {
            "success": True,
            "data": {
                "umur": umur,
                "penghasilan": penghasilan,
                "cluster": cluster,
                "label": label_map[cluster]
            }
        }

        return jsonify(hasil)

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)