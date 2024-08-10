from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400

    data = request.get_json()
    
    try:
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        operator = data['operator']
    except (KeyError, ValueError):
        return jsonify({'error': 'Invalid input data'}), 400

    if operator == 'add':
        result = num1 + num2
    elif operator == 'subtract':
        result = num1 - num2
    elif operator == 'multiply':
        result = num1 * num2
    elif operator == 'divide':
        if num2 == 0:
            return jsonify({'error': 'Cannot divide by zero'}), 400
        result = num1 / num2
    else:
        return jsonify({'error': 'Invalid operator'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
