# Basic Calculator (Python)

A simple four-operation calculator built as a clean, well-tested Python
project. It runs entirely in the terminal with **no external dependencies** —
just Python.

## Features

- Add, subtract, multiply, divide
- Friendly interactive menu in the terminal
- Handles bad input gracefully (invalid numbers, division by zero)
- Core logic (`Calculator` class) fully separated from the menu interface
- Unit tests covering every operation and edge case

## Getting Started

Requires Python 3.8+.

```bash
# Clone the repository
git clone https://github.com/<your-username>/basic-calculator.git
cd basic-calculator

# Run the calculator
python calculator.py
```

## Running the Tests

```bash
python -m unittest discover tests
```

or, if you have pytest installed:

```bash
python -m pytest
```

## Example Session

```
==============================
       BASIC CALCULATOR
==============================
 1. Add        (+)
 2. Subtract   (-)
 3. Multiply   (*)
 4. Divide     (/)
 5. Quit
------------------------------
Choose an option (1-5): 1
Enter first number: 12
Enter second number: 8
  12 + 8 = 20
```

## Project Structure

```
basic-calculator/
├── calculator.py            # Calculator class + interactive menu
├── tests/
│   └── test_calculator.py   # Unit tests for all operations
├── README.md
└── .gitignore
```

## Design Notes

The math lives in the `Calculator` class, which knows nothing about the
terminal or menus. `run_menu()` is a thin interface over it. This makes the
core logic trivially testable and keeps the code easy to extend — adding a
new operation means one method on the class and one entry in the menu dict.
