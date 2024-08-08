import sys
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView

class LeaderboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Leaderboard")
        self.setGeometry(100, 100, 600, 400)

        # Create a central widget and set the layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create a table widget
        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)

        # Set up the table
        self.setup_table()

        # Apply custom styles
        self.apply_styles()

        # Set up animations
        self.setup_animations()

    def setup_table(self):
        # Example data
        data = [
            ("1", "Alice", "1000"),
            ("2", "Bob", "900"),
            ("3", "Charlie", "800"),
            ("4", "Diana", "700"),
            ("5", "Eve", "600"),
        ]

        # Set the number of rows and columns
        self.table_widget.setRowCount(len(data))
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Rank", "Name", "Score"])

        # Populate the table with data
        for row, (rank, name, score) in enumerate(data):
            self.table_widget.setItem(row, 0, QTableWidgetItem(rank))
            self.table_widget.setItem(row, 1, QTableWidgetItem(name))
            self.table_widget.setItem(row, 2, QTableWidgetItem(score))

        # Resize columns to fit contents
        header = self.table_widget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

    def apply_styles(self):
        # Define custom style sheet
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QTableWidget {
                border: 1px solid #ccc;
                gridline-color: #ccc;
            }
            QTableWidget::item {
                padding: 5px;
                border: 1px solid #ddd;
            }
            QHeaderView::section {
                background-color: #3f51b5;
                color: white;
                padding: 4px;
            }
        """)

    def setup_animations(self):
        # Animation for the table widget
        self.animation = QPropertyAnimation(self.table_widget, b"geometry")
        self.animation.setDuration(1000)
        self.animation.setStartValue(QRect(0, -self.height(), self.width(), self.height()))
        self.animation.setEndValue(QRect(0, 0, self.width(), self.height()))
        self.animation.setEasingCurve(QEasingCurve.InOutBounce)
        self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LeaderboardWindow()
    window.show()
    sys.exit(app.exec_())
