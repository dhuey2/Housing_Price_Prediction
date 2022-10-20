from flask import Flask, request, jsonify
import utilities

app = Flask(__name__)


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': utilities.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bed = int(request.form['bed'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': utilities.get_estimated_price(location, total_sqft, bed, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/test')
def hello():
    return "why no work?"


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    utilities.load_saved_artifacts()
    app.run(debug=True)



