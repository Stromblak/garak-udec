from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/prompt', methods=['POST'])
def prompt():
    try:
        # Get the input query from the request
        prompt = request.json.get('prompt')

        # Use the query engine to get a response
        response = prompt

        # Return the response in JSON format
        return jsonify({'response': response})

    except Exception as e:
        # Handle any exceptions and return an error message
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(port=5000)


# source ./bin/activate
# idslab2023@152.74.29.21
# idslab2023