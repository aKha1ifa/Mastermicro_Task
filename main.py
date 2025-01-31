import sys
import numpy as np
import re
import matplotlib
matplotlib.use("Qt5Agg")  # Ensure it works with PySide2
import matplotlib.pyplot as plt
from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QLineEdit, QPushButton, QMessageBox)
from PySide2.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class FunctionPlotter(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Function Solver and Plotter")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.func1_input = QLineEdit(self)
        self.func1_input.setPlaceholderText("Enter first function of x (e.g., 5*x^3 + 2*x)")

        self.func2_input = QLineEdit(self)
        self.func2_input.setPlaceholderText("Enter second function of x (e.g., x^2 - 4)")

        self.solve_button = QPushButton("Solve and Plot", self)
        self.solve_button.clicked.connect(self.solve_and_plot)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("f1(x):"))
        input_layout.addWidget(self.func1_input)
        input_layout.addWidget(QLabel("f2(x):"))
        input_layout.addWidget(self.func2_input)

        layout.addLayout(input_layout)
        layout.addWidget(self.solve_button)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

    def validate_and_transform(self, func_str):
        """Validate and transform the function string into a valid Python expression."""
        func_str = func_str.lower().replace('^', '**')
        if not re.match(r'^[0-9x*+\-\/().^ sqrtlog]+$', func_str):
            raise ValueError("Invalid characters in function.")
        func_str = func_str.replace('log10', 'np.log10').replace('sqrt', 'np.sqrt')
        return func_str

    def solve_and_plot(self):
        func1_str = self.func1_input.text().strip()
        func2_str = self.func2_input.text().strip()

        try:
            # Validate and transform the input functions
            func1_str = self.validate_and_transform(func1_str)
            func2_str = self.validate_and_transform(func2_str)

            # Generate x values
            x = np.linspace(-10, 10, 400)

            # Evaluate the functions
            y1 = eval(func1_str, {"x": x, "np": np})
            y2 = eval(func2_str, {"x": x, "np": np})

            # Clear the previous plot
            self.ax.clear()

            # Plot the functions
            self.ax.plot(x, y1, label=f"f1(x): {self.func1_input.text()}")
            self.ax.plot(x, y2, label=f"f2(x): {self.func2_input.text()}")

            # Find intersection points
            intersection_points = self.find_intersections(x, y1, y2)

            if intersection_points:
                for point in intersection_points:
                    self.ax.scatter(point[0], point[1], color='red', zorder=3)
                    self.ax.annotate(f'({point[0]:.2f}, {point[1]:.2f})', (point[0], point[1]),
                                     textcoords="offset points", xytext=(5, 5), ha='right')

                # Center the plot around the first intersection point
                self.ax.set_xlim(intersection_points[0][0] - 5, intersection_points[0][0] + 5)
                self.ax.set_ylim(intersection_points[0][1] - 5, intersection_points[0][1] + 5)

            # Add title and axis labels
            self.ax.set_title("Function Plot")
            self.ax.set_xlabel("x")
            self.ax.set_ylabel("y")

            # Add grid and legend
            self.ax.axhline(0, color='black', linewidth=0.5)
            self.ax.axvline(0, color='black', linewidth=0.5)
            self.ax.grid(True, linestyle='--', linewidth=0.5)
            self.ax.legend()

            # Redraw the canvas
            self.canvas.draw()

        except ValueError as e:
            # Show error message for invalid input
            QMessageBox.critical(self, "Error", f"Invalid function input: {e}")
            # Clear the plot on error
            self.ax.clear()
            self.canvas.draw()
        except Exception as e:
            # Show error message for unexpected errors
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")
            # Clear the plot on error
            self.ax.clear()
            self.canvas.draw()

    def find_intersections(self, x, y1, y2):
        """Find precise intersection points between two curves."""
        intersections = []
        for i in range(len(x) - 1):
            # Check if the curves cross between x[i] and x[i+1]
            if (y1[i] - y2[i]) * (y1[i + 1] - y2[i + 1]) < 0:
                # Linear interpolation to find the intersection point
                x0 = x[i]
                x1 = x[i + 1]
                y10 = y1[i]
                y11 = y1[i + 1]
                y20 = y2[i]
                y21 = y2[i + 1]

                # Solve for x where y1 = y2
                x_intersect = x0 + (x1 - x0) * (y20 - y10) / ((y11 - y10) - (y21 - y20))
                y_intersect = y10 + (y11 - y10) * (x_intersect - x0) / (x1 - x0)

                intersections.append((x_intersect, y_intersect))
        return intersections


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FunctionPlotter()
    window.show()
    sys.exit(app.exec_())