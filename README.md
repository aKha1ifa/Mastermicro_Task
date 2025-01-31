# Mastermicro_Task
# Master Equation Solver Application



## Overview

The Equation Solver Application is a powerful tool designed to solve various types of mathematical equations. Whether you're dealing with linear equations, quadratic equations, or systems of equations, this application provides an intuitive interface and accurate solutions.

## Features

- Get solution points of two single-variable equations.
- User-Friendly Interface: Simple and intuitive interface for easy input and output.
- The Info button displays the differentiated and integrated equations.



## Technologies Used

- **Programming Language:** Python

### Libraries:
- matplotlib
- numpy
- PySide2
- **Testing:** Pytest, Pytest-qt

## Supported Operations

- Operators: `+`, `-`, `/`, `*`, `^`, `log10()`, `sqrt()`.
- Note: You can write logarithmic operations in two ways: `log10(x)` and `log(x, 10)`.

## Working Examples

### 1.1 One Intersection Point

**Output:**
- The plot shows the two functions intersecting at one point.
- The intersection point is annotated with its coordinates.

![One Intersection Point](https://raw.githubusercontent.com/aKha1ifa/Mastermicro_Task/refs/heads/main/Screenshot%202025-01-31%20at%208.13.32%E2%80%AFPM.png?token=GHSAT0AAAAAAC56YEQ7F3OBUIGOD67M32J6Z45D5BQ)  <!-- Update with actual image path -->

### 1.2 Multiple Intersection Points
**Input:**
- \( f_1(x): \sin(x) \)
- \( f_2(x): 0.5 \)

**Output:**
- The plot shows the two functions intersecting at multiple points.
- Each intersection point is annotated with its coordinates.

![Multiple Intersection Points](path/to/multiple_intersection_points_screenshot.png)  <!-- Update with actual image path -->

## Wrong Examples

### 2.1 Empty Input
**Input:** Leave one or both input fields empty.

**Output:** An error message is displayed: 
![Empty Input](path/to/empty_input_screenshot.png)  <!-- Update with actual image path -->

### 2.2 Invalid Character Input
**Input:**
- \( f_1(x): 3*x + 2 \)
- \( f_2(x): x^2 - 4 + @ \)

**Output:** An error message is displayed: 
![Invalid Character](path/to/invalid_character_screenshot.png)  <!-- Update with actual image path -->

### 2.3 Wrong Equation Input
**Input:**
- \( f_1(x): 3*x + 2 \)
- \( f_2(x): x^2 - 4 + \log(x) \) (invalid for \( x \leq 0 \))

**Output:** An error message is displayed: 
