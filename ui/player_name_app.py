from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QPushButton, QCheckBox, QLabel, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt
from ui.start_game import SecondWindow

class PlayerNameApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Player Name Entry")
        self.setGeometry(100, 100, 800, 400)  # Set a default size

        # Create a main layout
        main_layout = QVBoxLayout()  # Use vertical layout for better alignment

        # Create a grid layout for player entry
        self.entry_layout = QGridLayout()

        # Create a text box with a placeholder
        self.player_name_input = QLineEdit(self)
        self.player_name_input.setPlaceholderText("Enter player name")
        self.player_name_input.setMinimumHeight(50)  # Increase height
        self.player_name_input.setMinimumWidth(300)  # Increase width
        self.player_name_input.setStyleSheet("font-size: 20px;")  # Set font size

        # Create an "Add" button
        self.add_button = QPushButton("Add", self)
        self.add_button.setMinimumHeight(50)  # Increase height
        self.add_button.setMinimumWidth(100)   # Increase width
        self.add_button.setStyleSheet("font-size: 20px;")  # Set font size
        self.add_button.clicked.connect(self.add_player)

        # Create an "Edit" button
        self.edit_button = QPushButton("Edit", self)
        self.edit_button.setMinimumHeight(50)  # Increase height
        self.edit_button.setMinimumWidth(100)   # Increase width
        self.edit_button.setStyleSheet("font-size: 20px;")  # Set font size
        self.edit_button.clicked.connect(self.edit_player)

        # Create a QLabel for players
        self.players_label = QLabel("Players:", self)
        self.players_label.setStyleSheet("font-size: 20px;")  # Set font size

        # Layout to hold player checkboxes
        self.players_layout = QGridLayout()

        # Add widgets to the grid layout
        self.entry_layout.addWidget(self.player_name_input, 0, 0)  # Row 0, Column 0
        self.entry_layout.addWidget(self.add_button, 0, 1)          # Row 0, Column 1
        self.entry_layout.addWidget(self.edit_button, 0, 2)         # Row 0, Column 2
        self.entry_layout.addWidget(self.players_label, 1, 0)       # Row 1, Column 0
        self.entry_layout.addLayout(self.players_layout, 2, 0, 1, 3) # Row 2, Column 0 spanning 3 columns

        player_name = ['KAUSAR', 'SHAMS', 'SHAHNAWAZ', 'FARHAN', 'SHAQUIB']
        # Store players and checkboxes for editing
        self.Allplayer_checkboxes = []
        for i in player_name:
            player_checkbox = QCheckBox(i, self)
            player_checkbox.setStyleSheet("font-size: 18px;")  # Set font size for checkbox
            self.players_layout.addWidget(player_checkbox) 
            self.Allplayer_checkboxes.append(player_checkbox)

        # Add the entry layout to the main layout
        main_layout.addLayout(self.entry_layout)

        # Create a spacer to push the button to the bottom
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Create the "Start Game" button
        self.start_game_button = QPushButton("Start Game", self)
        #self.start_game_button.setDisabled(True)
        self.start_game_button.setMinimumHeight(50)  # Increase height
        self.start_game_button.setMinimumWidth(200)   # Increase width
        self.start_game_button.setStyleSheet("font-size: 20px;")  # Set font size
        main_layout.addWidget(self.start_game_button, alignment=Qt.AlignCenter)  # Add to main layout with center alignment
        self.start_game_button.clicked.connect(self.start_game)

        # Set the layout for the window
        self.setLayout(main_layout)        
        self.current_editing_checkbox = None  # Track the checkbox being edited

    def add_player(self):
        player_name = self.player_name_input.text()
        #print(f'Player Naame :::   {player_name}')
        if player_name:  # Only add if input is not empty
            # Create a new checkbox for the player
            player_checkbox = QCheckBox(player_name, self)
            player_checkbox.setStyleSheet("font-size: 18px;")  # Set font size for checkbox
            self.players_layout.addWidget(player_checkbox)  # Add checkbox to the layout

            # Store the checkbox for editing
            self.Allplayer_checkboxes.append(player_checkbox)

            # Clear the input after adding
            self.player_name_input.clear()
        #print(f"Player checkbox :: {self.player_checkboxes[0].text()}"

        if len(self.Allplayer_checkboxes)!= 0:
            self.start_game_button.setEnabled(True)

    def edit_player(self):
        # If we are not currently editing, find the checked checkbox
        if not self.current_editing_checkbox:
            for checkbox in self.player_checkboxes:
                if checkbox.isChecked():
                    # Load the name into the input for editing
                    self.player_name_input.setText(checkbox.text())
                    self.current_editing_checkbox = checkbox  # Track the checkbox being edited
                    checkbox.setChecked(False)  # Uncheck the checkbox after loading
                    return
        else:
            # We are in editing mode, update the checkbox name
            new_name = self.player_name_input.text()
            if new_name:  # Only update if input is not empty
                self.current_editing_checkbox.setText(new_name)  # Update the checkbox with the new name
                self.player_name_input.clear()  # Clear the input
                self.current_editing_checkbox = None  # Reset editing state

    def start_game(self):
        selected_player = [i.text() for i in self.Allplayer_checkboxes if i.isChecked()]
        print(f"Selected players : {selected_player}")
        self.second_window = SecondWindow(selected_player)
        self.second_window.show()
