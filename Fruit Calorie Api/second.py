from flask import Flask, jsonify, request

# Create a Flask app
app = Flask(__name__)


# Dictionary containing fruits and their calorie counts
fruits = {
    # Calories per 100g
    "banana": {"calories": 89},
    "apple": {"calories": 52},
    "orange": {"calories": 62},
    # Add more fruits with their calorie counts here
}


# Endpoint to list all fruits and their calorie counts
@app.route('/fruits', methods=['GET'])
def list_fruits():
    return jsonify(fruits)


# Endpoint to search for a fruit by its name
@app.route('/fruits/<name>', methods=['GET'])
def find_fruit(name):
    fruit = fruits.get(name.lower())
    if fruit:
        return jsonify(fruit)  # Return the fruit and its calorie count if found
    else:
        return jsonify({"message": "Fruit not found"}), 404  # Return a 404 error if the fruit is not found


# Endpoint to add a new fruit
@app.route('/fruits', methods=['POST'])
def add_fruit():
    data = request.get_json()  # Get JSON data from the request body
    name = data.get('name')
    calories = data.get('calories')
    if name and calories:
        fruits[name.lower()] = {'calories': calories}  # Add the new fruit to the dictionary
        return jsonify({"message": "Fruit added successfully"}), 201  # Return a success message and 201 status code
    else:
        return jsonify({"message": "Invalid request"}), 400  # Return an error message and 400 status code if request is invalid


# Endpoint to update the calorie count of a fruit
@app.route('/fruits/<name>', methods=['PUT'])
def update_fruit(name):
    fruit = fruits.get(name.lower())
    if fruit:
        data = request.get_json()
        calories = data.get('calories')
        if calories:
            fruit['calories'] = calories  # Update the calorie count of the fruit
            return jsonify({"message": "Calories updated successfully"})  # Return a success message
        else:
            return jsonify({"message": "Invalid request"}), 400  # Return an error message and 400 status code if request is invalid
    else:
        return jsonify({"message": "Fruit not found"}), 404  # Return a 404 error if the fruit is not found


# Endpoint to delete a fruit
@app.route("/fruits/<name>", methods=['DELETE'])
def delete_fruit(name):
    fruit = fruits.pop(name.lower(), None)  # Remove the fruit from the dictionary if it exists
    if fruit:
        return jsonify({"message": "Fruit deleted successfully"})  # Return a success message
    else:
        return jsonify({"message": "Fruit not found"}), 404  # Return a 404 error if the fruit is not found


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
