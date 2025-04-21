from flask import Flask, render_template, request, jsonify, send_file
import math
import json
import os
from datetime import datetime

app = Flask(__name__)

# Initialize history file path
HISTORY_FILE = 'calculator_history.json'

class Calculator:
    @staticmethod
    def load_history():
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, 'r') as f:
                return json.load(f)
        return []

    @staticmethod
    def save_history(history):
        with open(HISTORY_FILE, 'w') as f:
            json.dump(history, f)

    @staticmethod
    def add_to_history(operation, result):
        history = Calculator.load_history()
        history.append({
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'operation': operation,
            'result': result
        })
        # Keep only last 100 entries
        if len(history) > 100:
            history = history[-100:]
        Calculator.save_history(history)

    @staticmethod
    def clear_history():
        Calculator.save_history([])

    @staticmethod
    def export_history():
        history = Calculator.load_history()
        return json.dumps(history, indent=2)

    @staticmethod
    def calculate_area(shape, dimensions):
        if shape == 'square':
            side = float(dimensions['side'])
            return side * side
        elif shape == 'rectangle':
            length = float(dimensions['length'])
            width = float(dimensions['width'])
            return length * width
        elif shape == 'triangle':
            base = float(dimensions['base'])
            height = float(dimensions['height'])
            return 0.5 * base * height
        elif shape == 'circle':
            radius = float(dimensions['radius'])
            return math.pi * radius * radius
        elif shape == 'trapezoid':
            base1 = float(dimensions['base1'])
            base2 = float(dimensions['base2'])
            height = float(dimensions['height'])
            return 0.5 * (base1 + base2) * height
        elif shape == 'parallelogram':
            base = float(dimensions['base'])
            height = float(dimensions['height'])
            return base * height
        elif shape == 'pentagon':
            side = float(dimensions['side'])
            return (5 * side * side * math.cos(math.pi/5)) / (4 * math.sin(math.pi/5))
        elif shape == 'hexagon':
            side = float(dimensions['side'])
            return ((3 * math.sqrt(3)) / 2) * side * side
        elif shape == 'ellipse':
            majorAxis = float(dimensions['majorAxis'])
            minorAxis = float(dimensions['minorAxis'])
            return math.pi * majorAxis * minorAxis
        return 0

    @staticmethod
    def evaluate_expression(expression):
        try:
            # Replace sqrt with math.sqrt
            expression = expression.replace('√', 'math.sqrt')
            
            # Handle exponentiation
            expression = expression.replace('^', '**')
            
            # Create a safe dictionary of allowed names
            safe_dict = {
                'math': math,
                'sqrt': math.sqrt,
                'pi': math.pi,
                'e': math.e,
                'sin': math.sin,
                'cos': math.cos,
                'tan': math.tan,
                'log': math.log,
                'log10': math.log10,
                'exp': math.exp
            }
            
            # Evaluate the expression in a safe context
            result = eval(expression, {"__builtins__": {}}, safe_dict)
            
            # Format the result
            if isinstance(result, (int, float)):
                if result.is_integer():
                    return str(int(result))
                return f"{result:.8f}".rstrip('0').rstrip('.')
            return str(result)
        except Exception as e:
            return f"Error: {str(e)}"

    @staticmethod
    def validate_input(value):
        try:
            num = float(value)
            return num > 0
        except (ValueError, TypeError):
            return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    
    # Handle area calculations
    if 'shape' in data:
        shape = data.get('shape')
        dimensions = data.get('dimensions', {})
        
        # Validate all dimensions
        for key, value in dimensions.items():
            if not Calculator.validate_input(value):
                return jsonify({'error': f'Invalid input for {key}'}), 400
        
        try:
            area = Calculator.calculate_area(shape, dimensions)
            # Add to history
            operation = f"Area of {shape}: {dimensions}"
            Calculator.add_to_history(operation, f"{area:.2f} square units")
            return jsonify({'area': round(area, 2)})
        except (ValueError, KeyError) as e:
            return jsonify({'error': str(e)}), 400
    
    # Handle calculator expressions
    elif 'expression' in data:
        expression = data.get('expression')
        try:
            result = Calculator.evaluate_expression(expression)
            # Add to history
            Calculator.add_to_history(expression, result)
            return jsonify({'result': result})
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    
    return jsonify({'error': 'Invalid request'}), 400

@app.route('/history', methods=['GET', 'DELETE'])
def handle_history():
    if request.method == 'GET':
        history = Calculator.load_history()
        return jsonify(history)
    elif request.method == 'DELETE':
        Calculator.clear_history()
        return jsonify({'message': 'History cleared'})

@app.route('/export-history', methods=['GET'])
def export_history():
    history_text = Calculator.export_history()
    return send_file(
        history_text,
        mimetype='application/json',
        as_attachment=True,
        download_name='calculator_history.json'
    )

if __name__ == '__main__':
    app.run(debug=True) 