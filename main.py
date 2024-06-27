import random

from flask import Flask, jsonify

app = Flask(__name__)

first_names = [
    "Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry",
    "Iris", "Jack", "Kate", "Liam", "Mia", "Noah", "Olivia"
]
last_names = [
    "Smith", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
    "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson"
]


@app.route('/')
def index():
    return jsonify({"hello": "world"})


@app.route('/generate_name')
def generate_name():
    first = random.choice(first_names)
    last = random.choice(last_names)
    name = f"{first} {last}"
    return jsonify({'name': name})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
