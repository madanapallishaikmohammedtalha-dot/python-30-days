import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

def on_button_click():
    print("Button was clicked!")

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Tuition Management System")
window.resize(400, 300)

label = QLabel("Hello, Tuition System!", window)
label.move(140, 130)
label.resize(200,30)

# Add a button
button = QPushButton("Click Me", window)
button.move(150, 170)

# Connect the button's signal to our function
button.clicked.connect(on_button_click)

window.show()
app.exec()