"""
A basic calculator with a simple terminal menu.

Core logic lives in the Calculator class; the menu in main() is just a
thin interface over it. This separation keeps the math easy to test.

Usage:
    python calculator.py
"""

from __future__ import annotations

import sys


class Calculator:
    """A four-operation calculator.

    Each method takes two numbers and returns the result.
    Division by zero raises ZeroDivisionError — callers decide
    how to present it to the user.
    """

    def add(self, a: float, b: float) -> float:
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Return a minus b."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Return the product of a and b."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Return a divided by b.

        Raises:
            ZeroDivisionError: if b is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b


def read_number(prompt: str) -> float:
    """Ask until the user enters a valid number."""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("  Please enter a valid number (e.g. 12, -3.5).")


MENU = """
==============================
       BASIC CALCULATOR
==============================
 1. Add        (+)
 2. Subtract   (-)
 3. Multiply   (*)
 4. Divide     (/)
 5. Quit
------------------------------
"""


def run_menu() -> None:
    """Run the interactive menu loop."""
    calc = Calculator()
    actions = {
        "1": ("+", calc.add),
        "2": ("-", calc.subtract),
        "3": ("*", calc.multiply),
        "4": ("/", calc.divide),
    }

    while True:
        print(MENU)
        choice = input("Choose an option (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            sys.exit(0)

        if choice not in actions:
            print("  Invalid choice — please enter 1, 2, 3, 4 or 5.")
            continue

        symbol, operation = actions[choice]
        a = read_number("Enter first number: ")
        b = read_number("Enter second number: ")

        try:
            result = operation(a, b)
        except ZeroDivisionError as err:
            print(f"  Error: {err}")
            continue

        print(f"  {a:g} {symbol} {b:g} = {result:g}")


if __name__ == "__main__":
    run_menu()
