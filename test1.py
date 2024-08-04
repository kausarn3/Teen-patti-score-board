import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QFormLayout,
    QHBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor

class QuadrantWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle("Enhanced Quadrant Layout")
        self.setGeometry(100, 100, 800, 600)

        # Create a grid layout
        self.grid_layout = QGridLayout()
        
        self.playArea() #form layout to the first quadrant
        self.scoreArea() # Second Quadrant: Label

        
        # Third Quadrant: Label
        label2 = QLabel("This is the third quadrant")
        label2.setAlignment(Qt.AlignCenter)
        label2.setStyleSheet("font-size: 18px; background-color: #f0f0f0; padding: 20px; border: 1px solid #ccc; border-radius: 10px;")

        self.grid_layout.addWidget(label2, 1, 0)  # Row 1, Column 0

        # Fourth Quadrant: Label
        label3 = QLabel("This is the fourth quadrant")
        label3.setAlignment(Qt.AlignCenter)
        label3.setStyleSheet("font-size: 18px; background-color: #f0f0f0; padding: 20px; border: 1px solid #ccc; border-radius: 10px;")

        self.grid_layout.addWidget(label3, 1, 1)  # Row 1, Column 1

        # Set the layout for the main window
        self.setLayout(self.grid_layout)

        # Set a main window background color
        self.setStyleSheet("background-color: #e0e0e0;")

    def playArea(self):
        form_layout = QFormLayout()
        #form_layout.setContentsMargins(20, 20, 20, 20)  # Add margins to the layout
        #form_layout.setSpacing(15)  # Set spacing between rows
        font = QFont("Arial", 12)
        submit_button = QPushButton("Submit")
        # Add rows to the form layout
        player_names = ['Player 1', 'Player 2', 'Player 3', 'Player 4']
        self.name_inputs = []  # Store input fields for later use
        for player in player_names:
            name_input = QLineEdit()
            name_input.setStyleSheet("""
    QLineEdit {
        background-color: #ffffff; /* White background */
        border: 2px solid #ccc; /* Light gray border */
        border-radius: 5px; /* Rounded corners */
        padding: 10px; /* Padding inside the input */
        font-size: 14px; /* Font size */
        color: #333; /* Text color */
    }
    
    QLineEdit:focus {
        border: 2px solid #4CAF50; /* Green border when focused */
        background-color: #f9f9f9; /* Slightly darker background when focused */
    }
    
    QLineEdit::placeholder {
        color: #aaa; /* Placeholder text color */
        font-style: italic; /* Italicize placeholder text */
    }
""")

            name_label = QLabel(f"{player} : ")
            name_label.setFont(font)
            name_input.setPlaceholderText(f"{player}")
            #name_input.setFont(font)  # Set font for QLineEdit
            #name_input.setStyleSheet("QLineEdit { padding: 10px; border: 1px solid #ccc; border-radius: 5px; }")
            form_layout.addRow(name_label, name_input)
            self.name_inputs.append(name_input)  # Keep track of input fields

        # Style the submit button
        submit_button = QPushButton("Submit")
        submit_button.setFont(font)
        submit_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;  /* Green */
                color: white;
                padding: 10px;
                border: none;
                border-radius: 5px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        submit_button.setFixedSize(120, 40)
        button_layout = QHBoxLayout()
        button_layout.addWidget(submit_button, alignment=Qt.AlignCenter)

        # Add the submit button to the layout
        form_layout.addRow(button_layout)
        form_widget = QWidget()
        form_widget.setLayout(form_layout)
        form_widget.setFixedSize(600, 500)  # Fixed size for the form layout
        self.grid_layout.addWidget(form_widget, 0, 0)

    def scoreArea(self):
        label1 = QLabel("ScoreBoard")
        #label1.setAlignment(Qt.AlignCenter)
        label1.setStyleSheet("font-size: 18px; background-color: #8B0000; padding: 20px; border: 1px solid #ccc; border-radius: 10px;")
        self.grid_layout.addWidget(label1, 0, 1)  # Row 0, Column 1




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuadrantWindow()
    window.show()
    sys.exit(app.exec_())
