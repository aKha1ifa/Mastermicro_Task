import pytest
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Qt
from main import FunctionPlotter


@pytest.fixture
def app(qtbot):
    """Fixture to create the application and main window."""
    application = QApplication.instance()
    if application is None:
        application = QApplication([])
    window = FunctionPlotter()
    qtbot.addWidget(window)
    return window


def test_valid_function_input(app, qtbot):
    """Test valid function input and plotting."""
    app.func1_input.setText("x**2")
    app.func2_input.setText("2*x + 1")
    qtbot.mouseClick(app.solve_button, Qt.LeftButton)

    # Verify that the plot is generated without errors
    assert app.ax.lines, "No lines were plotted"

    # Filter out lines that are not function plots (e.g., grid lines, axes lines)
    function_labels = [f"f1(x): {app.func1_input.text()}", f"f2(x): {app.func2_input.text()}"]
    function_lines = [line for line in app.ax.lines if line.get_label() in function_labels]

    assert len(function_lines) == 2, "Expected two lines to be plotted"


def test_invalid_function_input(app, qtbot):
    """Test invalid function input."""
    app.func1_input.setText("x**2")
    app.func2_input.setText("invalid_function")
    qtbot.mouseClick(app.solve_button, Qt.LeftButton)

    # Verify that an error message is displayed and no lines are plotted
    assert not app.ax.lines, "Lines were plotted despite invalid input"


def test_intersection_points(app, qtbot):
    """Test intersection points are correctly annotated."""
    app.func1_input.setText("x**2")
    app.func2_input.setText("2*x + 1")
    qtbot.mouseClick(app.solve_button, Qt.LeftButton)

    # Verify that intersection points are annotated
    assert len(app.ax.collections) > 0, "No intersection points were annotated"
    for collection in app.ax.collections:
        assert collection.get_offsets().data.size > 0, "No intersection points were annotated"


if __name__ == "__main__":
    pytest.main()