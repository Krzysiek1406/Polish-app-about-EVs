from main_okno import Main_okno
import sys
from PyQt6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    # input("Press Enter to exit...")
    main_window = Main_okno()
    sys.exit(app.exec())



if __name__ == '__main__':
    main()
