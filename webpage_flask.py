from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load precomputed data from JSON file
with open("precomputed_data.json", "r") as f:
    precomputed_data = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_path", methods=["POST"])
def get_path():
    source = request.form.get("source")
    destination = request.form.get("destination")

    # Retrieve precomputed path based on source
    path = precomputed_data.get(source, {}).get(destination, None)

    if path:
        return jsonify({"path": path}), 200, {'Content-Type': 'application/json'}
    else:
        return jsonify({"error": "No path found for the given source and destination."}), 404, {'Content-Type': 'application/json'}

if __name__ == "__main__":
    app.run(debug=True)
