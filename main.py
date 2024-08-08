import sys
from PyQt5.QtWidgets import QApplication
from ui.player_name_app import PlayerNameApp

def main():
    app = QApplication(sys.argv)
    window = PlayerNameApp()
    window.show()
    #window.showMaximized()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
