# Math Tools Calculator

A modern web-based calculator with advanced features including area calculations and calculation history.

## Features

- **Basic Calculator**
  - Standard arithmetic operations (+, -, ×, ÷)
  - Advanced operations (√, ^)
  - Parentheses support
  - Clear display functionality
  - Error handling

- **Area Calculator**
  - Support for multiple shapes:
    - Square
    - Rectangle
    - Triangle
    - Circle
    - Trapezoid
    - Parallelogram
    - Regular Pentagon
    - Regular Hexagon
    - Ellipse
  - Real-time calculations
  - Input validation

- **Calculation History**
  - Stores last 100 calculations
  - Timestamp for each calculation
  - Easy access via clock button
  - Clear history option
  - Compact and non-intrusive design

## Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- Bootstrap 5

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install dependencies:
```bash
pip install flask
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## Usage

### Basic Calculator
- Click the number and operator buttons to input calculations
- Press '=' to see the result
- Use 'C' to clear the display
- Keyboard support for all operations

### Area Calculator
1. Select a shape from the dropdown
2. Enter the required dimensions
3. Click "Calculate Area" to see the result

### History
- Click the clock icon (🕒) in the top right to view calculation history
- Use the clear button to remove all history
- History automatically updates after each calculation

## Project Structure

```
├── app.py              # Flask application
├── templates/
│   └── index.html      # Main calculator interface
└── calculator_history.json  # Stores calculation history
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License. 