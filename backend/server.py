from flask import Flask, request, jsonify

app = Flask(__name__)

buses = [
    {"id": 1, "route": "101A", "latitude": 40.730610, "longitude": -73.935242, "arrival_time": "08:15", "driver_contact": "123-456-7890"},
    {"id": 2, "route": "102B", "latitude": 40.741895, "longitude": -73.989308, "arrival_time": "08:20", "driver_contact": "123-456-7891"},
]

@app.route("/buses", methods=["GET"])
def get_buses():
    return jsonify(buses) 

if __name__ == "__main__":
    app.run(debug=True)
