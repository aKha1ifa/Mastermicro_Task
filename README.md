# Mastermicro_Task
Function Plotter Application
This is a Python-based application that allows users to input two mathematical functions of x, solves for their intersection points, and plots the functions along with the intersection points. The application is built using PySide2 for the GUI and matplotlib for plotting.

Features
Input two functions of x (e.g., 3*x + 2, x^2 - 4).

Plot the functions and highlight their intersection points.

Annotate the intersection points with their coordinates.

Handle invalid inputs and display appropriate error messages.

Installation
Prerequisites:

Python 3.x

Required libraries: PySide2, numpy, matplotlib

Install Dependencies:

bash
Copy
pip install PySide2 numpy matplotlib
Run the Application:

bash
Copy
python function_plotter.py
Working Examples
1.1 One Intersection Point
Input:

f1(x): 3*x + 2

f2(x): x^2 - 4

Output:

The plot shows the two functions intersecting at one point.

The intersection point is annotated with its coordinates.

One Intersection Point

1.2 Multiple Intersection Points
Input:

f1(x): sin(x)

f2(x): 0.5

Output:

The plot shows the two functions intersecting at multiple points.

Each intersection point is annotated with its coordinates.

Multiple Intersection Points

Error Handling Examples
2.1 Empty Input
Input:

Leave one or both input fields empty.

Output:

An error message is displayed: "Invalid function input: Empty input."

Empty Input

2.2 Invalid Character
Input:

f1(x): 3*x + 2

f2(x): x^2 - 4 + @

Output:

An error message is displayed: "Invalid function input: Invalid characters in function."

Invalid Character

2.3 Wrong Equation
Input:

f1(x): 3*x + 2

f2(x): x^2 - 4 + log(x) (invalid for x <= 0)

Output:

An error message is displayed: "An unexpected error occurred: math domain error."

Wrong Equation
