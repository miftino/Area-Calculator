from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

class Calculator:
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
            return jsonify({'area': round(area, 2)})
        except (ValueError, KeyError) as e:
            return jsonify({'error': str(e)}), 400
    
    # Handle calculator expressions
    elif 'expression' in data:
        expression = data.get('expression')
        try:
            result = Calculator.evaluate_expression(expression)
            return jsonify({'result': result})
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    
    return jsonify({'error': 'Invalid request'}), 400

if __name__ == '__main__':
    app.run(debug=True) 