// Initialize the page
document.addEventListener('DOMContentLoaded', function() {
    // Show the initial shape inputs (square)
    document.getElementById('square-inputs').classList.add('active');
    
    // Add event listener for shape selection
    document.getElementById('shape').addEventListener('change', function() {
        // Hide all input sections
        document.querySelectorAll('.shape-inputs').forEach(el => {
            el.classList.remove('active');
        });
        
        // Show the selected shape's input section
        const selectedShape = this.value;
        document.getElementById(selectedShape + '-inputs').classList.add('active');
    });

    // Add keyboard support for calculator
    document.addEventListener('keydown', function(event) {
        const key = event.key;
        const display = document.getElementById('calc-display');
        const activeTab = document.querySelector('.nav-link.active').id;
        
        // Only prevent default for calculator keys when in calculator tab
        if (activeTab === 'calc-tab') {
            if (/[0-9+\-*/.()=^]/.test(key) || 
                key === 'Enter' || 
                key === 'Backspace' || 
                key === 'Escape') {
                event.preventDefault();
            }
            
            // Handle number keys
            if (/[0-9]/.test(key)) {
                appendToDisplay(key);
            }
            // Handle operators
            else if (['+', '-', '*', '/', '^'].includes(key)) {
                appendToDisplay(key);
            }
            // Handle decimal point
            else if (key === '.') {
                appendToDisplay('.');
            }
            // Handle parentheses
            else if (key === '(' || key === ')') {
                appendToDisplay(key);
            }
            // Handle equals/enter
            else if (key === '=' || key === 'Enter') {
                calculate();
            }
            // Handle backspace
            else if (key === 'Backspace') {
                display.value = display.value.slice(0, -1);
            }
            // Handle escape (clear)
            else if (key === 'Escape') {
                clearDisplay();
            }
        }
    });
});

// Input validation functions
function validateNumberInput(input) {
    const value = parseFloat(input);
    return !isNaN(value) && isFinite(value) && value >= 0;
}

function validateCalculatorInput(value) {
    const display = document.getElementById('calc-display');
    const currentValue = display.value;
    
    // Prevent multiple operators in sequence
    if (['+', '-', '*', '/', '^'].includes(value)) {
        const lastChar = currentValue[currentValue.length - 1];
        if (['+', '-', '*', '/', '^'].includes(lastChar)) {
            return false;
        }
    }
    
    // Prevent multiple decimal points in a number
    if (value === '.') {
        const lastNumber = currentValue.split(/[\+\-\*\/\^\(\)]/).pop();
        if (lastNumber.includes('.')) {
            return false;
        }
    }
    
    // Prevent invalid parentheses
    if (value === '(') {
        const lastChar = currentValue[currentValue.length - 1];
        if (/[0-9.]/.test(lastChar)) {
            return false;
        }
    }
    
    if (value === ')') {
        const openCount = (currentValue.match(/\(/g) || []).length;
        const closeCount = (currentValue.match(/\)/g) || []).length;
        if (openCount <= closeCount) {
            return false;
        }
    }
    
    return true;
}

// Update appendToDisplay function
function appendToDisplay(value) {
    const display = document.getElementById('calc-display');
    if (display.value === 'Error') {
        display.value = '';
        display.classList.remove('error');
    }
    
    if (!validateCalculatorInput(value)) {
        return;
    }
    
    display.value += value;
}

function clearDisplay() {
    const display = document.getElementById('calc-display');
    display.value = '';
    display.classList.remove('error');
}

function handleSqrt() {
    const display = document.getElementById('calc-display');
    if (display.value === 'Error') {
        clearDisplay();
        return;
    }
    appendToDisplay('√(');
}

// Update calculateArea function
function calculateArea() {
    const shape = document.getElementById('shape').value;
    let dimensions = {};
    let isValid = true;
    
    switch(shape) {
        case 'square':
            const side = document.getElementById('side').value;
            if (!validateNumberInput(side)) {
                showError('Please enter a valid side length');
                isValid = false;
                break;
            }
            dimensions.side = side;
            break;
            
        case 'rectangle':
            const length = document.getElementById('length').value;
            const width = document.getElementById('width').value;
            if (!validateNumberInput(length) || !validateNumberInput(width)) {
                showError('Please enter valid length and width');
                isValid = false;
                break;
            }
            dimensions.length = length;
            dimensions.width = width;
            break;
            
        case 'triangle':
            const base = document.getElementById('base').value;
            const height = document.getElementById('height').value;
            if (!validateNumberInput(base) || !validateNumberInput(height)) {
                showError('Please enter valid base and height');
                isValid = false;
                break;
            }
            dimensions.base = base;
            dimensions.height = height;
            break;
            
        case 'circle':
            const radius = document.getElementById('radius').value;
            if (!validateNumberInput(radius)) {
                showError('Please enter a valid radius');
                isValid = false;
                break;
            }
            dimensions.radius = radius;
            break;
            
        case 'trapezoid':
            const base1 = document.getElementById('base1').value;
            const base2 = document.getElementById('base2').value;
            const trapezoidHeight = document.getElementById('trapezoid-height').value;
            if (!validateNumberInput(base1) || !validateNumberInput(base2) || !validateNumberInput(trapezoidHeight)) {
                showError('Please enter valid base lengths and height');
                isValid = false;
                break;
            }
            dimensions.base1 = base1;
            dimensions.base2 = base2;
            dimensions.height = trapezoidHeight;
            break;
            
        case 'parallelogram':
            const pBase = document.getElementById('parallelogram-base').value;
            const pHeight = document.getElementById('parallelogram-height').value;
            if (!validateNumberInput(pBase) || !validateNumberInput(pHeight)) {
                showError('Please enter valid base and height');
                isValid = false;
                break;
            }
            dimensions.base = pBase;
            dimensions.height = pHeight;
            break;
            
        case 'pentagon':
        case 'hexagon':
            const sideLength = document.getElementById(shape + '-side').value;
            if (!validateNumberInput(sideLength)) {
                showError('Please enter a valid side length');
                isValid = false;
                break;
            }
            dimensions.side = sideLength;
            break;
            
        case 'ellipse':
            const majorAxis = document.getElementById('major-axis').value;
            const minorAxis = document.getElementById('minor-axis').value;
            if (!validateNumberInput(majorAxis) || !validateNumberInput(minorAxis)) {
                showError('Please enter valid major and minor axes');
                isValid = false;
                break;
            }
            dimensions.majorAxis = majorAxis;
            dimensions.minorAxis = minorAxis;
            break;
    }
    
    if (!isValid) {
        return;
    }

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            shape: shape,
            dimensions: dimensions
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            showError(data.error);
        } else {
            document.getElementById('result').textContent = `Area: ${data.area} square units`;
            loadHistory();
        }
    })
    .catch(error => {
        showError('Error calculating area');
    });
}

// Add error display function
function showError(message) {
    const resultElement = document.getElementById('result');
    resultElement.textContent = message;
    resultElement.classList.add('error');
    setTimeout(() => {
        resultElement.classList.remove('error');
    }, 3000);
}

// Update calculate function
function calculate() {
    const display = document.getElementById('calc-display');
    const expression = display.value;
    
    // Validate expression before sending
    if (!expression) {
        showError('Please enter an expression');
        return;
    }
    
    // Check for balanced parentheses
    const openCount = (expression.match(/\(/g) || []).length;
    const closeCount = (expression.match(/\)/g) || []).length;
    if (openCount !== closeCount) {
        showError('Unbalanced parentheses');
        return;
    }
    
    // Check for invalid operator sequences
    if (/[\+\-\*\/\^]{2,}/.test(expression)) {
        showError('Invalid operator sequence');
        return;
    }
    
    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            expression: expression
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            display.value = 'Error';
            display.classList.add('error');
            showError(data.error);
        } else {
            display.value = data.result;
            loadHistory();
        }
    })
    .catch(error => {
        display.value = 'Error';
        display.classList.add('error');
    });
}

// History functionality
function toggleHistory() {
    const historyPanel = document.getElementById('historyPanel');
    historyPanel.classList.toggle('active');
}

function loadHistory() {
    fetch('/history')
        .then(response => response.json())
        .then(history => {
            const historyList = document.getElementById('historyList');
            historyList.innerHTML = '';
            history.reverse().forEach(item => {
                const historyItem = document.createElement('div');
                historyItem.className = 'history-item';
                historyItem.innerHTML = `
                    <div class="timestamp">${item.timestamp}</div>
                    <div class="operation">${item.operation}</div>
                    <div class="result">= ${item.result}</div>
                `;
                historyList.appendChild(historyItem);
            });
        });
}

function clearHistory() {
    if (confirm('Are you sure you want to clear the history?')) {
        fetch('/history', { method: 'DELETE' })
            .then(response => response.json())
            .then(() => {
                loadHistory();
            });
    }
} 