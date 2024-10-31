# Simple Calculator Using Tkinter

This is a simple calculator application built using Python's Tkinter library. The calculator supports basic arithmetic operations, memory functions, and keyboard input.

## Features
1. Basic arithmetic operations: addition, subtraction, multiplication, and division.
2. Memory functions: add to memory, clear memory, and recall memory.
3. Square root calculation.
4. Input validation to ensure only valid expressions are evaluated.
5. Keyboard support for inputting numbers and operations.

## Requirements
1. Python 3.x
2. Tkinter (usually included with Python installations)


## Installation

1. Clone the repository or download the source code.

   git clone https://github.com/subhankardash4474/Python-Project-Portfolio/tree/master/

2. Navigate to the project directory.

   cd Calculator

3. Run the application.

   python calculator.py

## Usage

* Input Numbers: Click on the number buttons or type the numbers using your keyboard.
* Input Operations: Click on the operation buttons (+, -, *, /, %) or type them using your keyboard.
* Calculate Result: Click on the = button or press Enter to calculate the result of the expression.
* Clear Input: Click on the AC button to clear the current input.
* Undo Last Input: Click on the <- button or press the Backspace key to remove the last character.
* Memory Functions:
  - M+: Adds the current display value to memory.
  - MC: Clears the memory.
  - MR: Recalls the value stored in memory.
* Square Root: Click on the √ button to calculate the square root of the current display value.

## Code Overview

* The main GUI is created using Tkinter.
* The calculator supports basic arithmetic operations and uses the ast module to validate expressions before evaluation.
* Memory functions are implemented to store, clear, and recall values.
* Keyboard input is handled using event binding.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request with your improvements or bug fixes.
