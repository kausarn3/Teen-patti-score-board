import sys
from PyQt5.QtWidgets import (
    QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QFormLayout,
    QHBoxLayout, QSplitter, QTextEdit, QVBoxLayout, QApplication, QTableWidget,
    QHeaderView
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a vertical splitter
        self.splitter = QSplitter(Qt.Horizontal)

        # Create the left part
        left_widget = QWidget()
        self.left_layout = QVBoxLayout()
        left_widget.setLayout(self.left_layout)

        # Add text edits to the left widget (half of the left part)
        self.playArea()
        self.scoreboard()
        
        # Add widgets to the splitter
        self.splitter.addWidget(left_widget)
        
        self.totalScore()

        # Set the main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.splitter)
        self.setLayout(main_layout)

        # Set the window title and size
        self.setWindowTitle("Split Layout Example")
        self.resize(800, 600)

    def playArea(self):
        form_layout = QFormLayout()
        font = QFont("Arial", 12)
        submit_button = QPushButton("Submit")
        # Add rows to the form layout
        self.name_inputs = []  # Store input fields for later use
        selected_players = ['Kausar', 'abc',5,6,9,8,9,9]
        for player in selected_players:
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
        # button_layout.clicked.connect(self.start_game)

        # Add the submit button to the layout
        form_layout.addRow(button_layout)
        self.left_layout.addLayout(form_layout)
        #self.left_layout.setFixedSize(600, 500) 

    def scoreboard(self):
        left_label = QLabel("This is a label below the form.")
        self.left_layout.addWidget(left_label)

    def totalScore(self):
        table_widget = QTableWidget()
        table_widget.setColumnCount(8)  # Number of columns
        table_widget.setRowCount(70)     # Number of rows (adjust as needed)
        table_widget.setHorizontalHeaderLabels(['Kausar', 'abc','5','6','9','8','9','9'])
        # Make the table scrollable
        table_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        table_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # Set table properties
        table_widget.horizontalHeader().setStretchLastSection(True)
        table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.splitter.addWidget(table_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
