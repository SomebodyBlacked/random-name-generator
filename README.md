# Random Name Generator API

This is a simple Flask API that generates random names. It uses a list of common first and last names to create a unique name each time the `/generate_name` endpoint is called.

## Usage

To use the API, simply make a GET request to the `/generate_name` endpoint. This will return a JSON object containing a randomly generated name.

**Example:**

```bash
curl http://localhost:5000/generate_name
```
**Output:**

```json
{
  "name": "Alice Smith"
}
```

## Running the API

To run the API, follow these steps:

1. Install the required dependencies:

```
pip install -r requirements.txt
```

2. Run the Flask app:

```
flask --app main.py run
```

The API will now be running on `http://127.0.0.1:5000/`

## Endpoints

The API has the following endpoint:

- `/generate_name`: Generates a random name and returns it as a JSON object.
- 