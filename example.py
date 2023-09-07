from flask import Flask, jsonify, request

app = Flask(__name__)

# API data
items = [
  {"userid": 325223, "username": "Bob", "subscription": "Basic", "joindate": "2-20-23", "role": "member"},
  {"userid": 564235, "username": "Sally", "subscription": "Basic", "joindate": "3-7-22", "role": "member"},
  {"userid": 092348, "username": "Pisscan", "subscription": "Pro", "joindate": "6-5-20", "role": "member"},
  {"userid": 094834, "username": "Nick2020", "subscription": "Pro", "joindate": "2-24-21", "role": "Admin"},
  {"userid": 235635, "username": "Ja$$on", "subscription": "Basic", "joindate": "12-1-22", "role": "member"},
]

# API endpoint to get all items
@app.route('/api', methods=['GET'])
def get_items():
    return jsonify({"items": items})

# API endpoint to get a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["userid"] == item_id), None)
    if item is None:
        return jsonify({"message": "Item not found"}), 404
    return jsonify({"userid": item})

# API endpoint to update item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    item = next((item for item in items if item["userid"] == item_id), None)
    if item is None:
        return jsonify({"message": "Item not found"}), 404

    item["name"] = data.get("username", item["username"])
    return jsonify({"item": item})

# API endpoint to delete an item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    item = next((item for item in items if item["userid"] == item_id), None)
    if item is None:
        return jsonify({"message": "Item not found"}), 404

    items = [item for item in items if item["id"] != item_id]
    return jsonify({"message": "Item deleted"})

if __name__ == '__main__':
    app.run(debug=True)
