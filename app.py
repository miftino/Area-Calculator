from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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
        return 3.14159 * radius * radius
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
        return (5 * side * side * Math.cos(Math.PI/5)) / (4 * Math.sin(Math.PI/5))
    elif shape == 'hexagon':
        side = float(dimensions['side'])
        return ((3 * Math.sqrt(3)) / 2) * side * side
    elif shape == 'ellipse':
        majorAxis = float(dimensions['majorAxis'])
        minorAxis = float(dimensions['minorAxis'])
        return Math.PI * majorAxis * minorAxis
    return 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    shape = data.get('shape')
    dimensions = data.get('dimensions', {})
    
    try:
        area = calculate_area(shape, dimensions)
        return jsonify({'area': round(area, 2)})
    except (ValueError, KeyError):
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True) 