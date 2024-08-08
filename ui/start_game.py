import sys
import pandas as pd
import os
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QFormLayout,
    QHBoxLayout, QSplitter, QVBoxLayout, QApplication, QTableWidget,
    QHeaderView, QTableWidgetItem, QStackedWidget
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor


class SecondWindow(QWidget):
    def __init__(self, selected_players):
        super().__init__()
        self.selected_players = selected_players
        
        # Create a vertical splitter
        self.splitter = QSplitter(Qt.Horizontal)

        # Create the left part
        left_widget = QWidget()
        self.left_layout = QVBoxLayout()
        left_widget.setLayout(self.left_layout)

        # Initialize components for the left part
        self.playArea()

        self.leaderboard_page = QWidget()
        self.leaderboard_layout = QVBoxLayout(self.leaderboard_page)
        # Sample player data
        self.total_score_table = QTableWidget()

        self.total_game_score = [0 for i in range(len(selected_players))]

        # Add widgets to the splitter
        self.splitter.addWidget(left_widget)
        # Create the right part with the scoreboard
        self.table_widget = self.totalScore()        

        # Set the main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.splitter)
        self.setLayout(main_layout)

        # Set the window title and size
        self.setWindowTitle("Score Board")
        self.resize(1000, 650)

    def playArea(self):
        form_layout = QFormLayout()
        font = QFont("Arial", 12)
        submit_button = QPushButton("Submit")
        # Add rows to the form layout
        self.name_inputs = []  # Store input fields for later use
        for player in self.selected_players:
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

        # Connect the submit button to the submit function
        submit_button.clicked.connect(self.submit_data)

        # Add the submit button to the layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(submit_button, alignment=Qt.AlignCenter)
        form_layout.addRow(button_layout)
        self.left_layout.addLayout(form_layout)

    def scoreboard(self, data):
        result = dict(zip(self.selected_players, data))
        result = sorted(result.items(), key=lambda item: item[1], reverse=True)
        # Setup table dimensions
        self.total_score_table.setRowCount(len(self.selected_players))  # Number of rows
        self.total_score_table.setColumnCount(2)  # Number of columns
        self.total_score_table.setHorizontalHeaderLabels(["Name", "Score"])
        self.total_score_table.horizontalHeader().setStyleSheet("QHeaderView::section { font-weight: bold; font-size: 14pt; }")
        # Fill the table with example data
        for i in enumerate(result):  
            score = i[1][1]
            name = i[1][0]
            name_item = QTableWidgetItem(name)
            score_item = QTableWidgetItem(str(score))            
            font = QFont()
            font.setBold(True)
            name_item.setFont(font)            
            score_item.setFont(font)
            if i[0] == 0:
                score_item.setBackground(QColor(200, 255, 200))
                name_item.setBackground(QColor(200, 255, 200))
            elif len(result)-1 == i[0]:
                 score_item.setBackground(QColor(255, 200, 200))
                 name_item.setBackground(QColor(255, 200, 200))            

            #self.total_score_table.setItem(i[0], 0, QTableWidgetItem(str(i[0] + 1)))  # Rank
            self.total_score_table.setItem(i[0], 0, name_item)  # Name
            self.total_score_table.setItem(i[0], 1, score_item)  # Score
        
    def totalScore(self):
        table_widget = QTableWidget()
        table_widget.setColumnCount(len(self.selected_players))  # Number of columns
        table_widget.setRowCount(0)      # Start with zero rows
        table_widget.setHorizontalHeaderLabels(self.selected_players)
        table_widget.horizontalHeader().setStyleSheet("QHeaderView::section { font-weight: bold; font-size: 14pt; }")


        # # Make the table scrollable
        table_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        table_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # Set table properties
        table_widget.horizontalHeader().setStretchLastSection(True)
        table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # Add the table widget to the splitter
        self.splitter.addWidget(table_widget)

        return table_widget

    def submit_data(self):
        # Retrieve data from input fields
        row_data = [input_field.text() for input_field in self.name_inputs]
        row_data = self.ret_calculated_value(row_data)
        winner = max([int(i)for i in row_data])
        looser = min([int(i)for i in row_data])

        # Add the row data to the table
        current_row_count = self.table_widget.rowCount()
        self.table_widget.insertRow(current_row_count)
        
        for column, data in enumerate(row_data):
            item = QTableWidgetItem(data)
            if int(data) == winner:
                item.setBackground(QColor(200, 255, 200))
            elif int(data) == looser:
                item.setBackground(QColor(255, 200, 200))
            
            font = QFont()
            font.setBold(True)
            item.setFont(font)
            self.table_widget.setItem(current_row_count, column, item)
        
        
        # Save the data to an Excel file
        self.save_to_excel(row_data)
        total_score = [x + int(y) for x,y in zip(self.total_game_score, row_data)]
        self.total_game_score = total_score
        self.scoreboard(total_score)
        self.leaderboard_layout.addWidget(self.total_score_table)
        self.left_layout.addWidget(self.leaderboard_page)
        for input_field in self.name_inputs:
            input_field.clear()

    def save_to_excel(self, row_data):
        # Define the Excel file path
        excel_file = 'scoreboard.xlsx'
        # Check if the file exists
        if os.path.exists(excel_file):
            # Read existing data from the Excel file
            df_existing = pd.read_excel(excel_file)
            # Append the new data to the existing DataFrame
            new_row = pd.DataFrame([row_data], columns=self.selected_players)
            df = pd.concat([df_existing, new_row], ignore_index=True)
        else:
            # Create a new DataFrame with the new row
            df = pd.DataFrame([row_data], columns=self.selected_players)

        # Save the updated DataFrame to the Excel file
        df.to_excel(excel_file, index=False)

    def ret_calculated_value(self, scores):
        sum_values = sum(int(value) for value in scores if value)
        result = [str(sum_values) if value == '' else str(-int(value)) for value in scores]
        return result
    
# app = QApplication(sys.argv)
# second_window = SecondWindow(["a","B","c","d","e"])
# second_window.show()
# sys.exit(app.exec_())