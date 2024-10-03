from PyQt6.QtWidgets import QPushButton, QApplication


class Zamykacz(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText("Zamknij aplikację")
        self.setStyleSheet(
            "QPushButton {"
            "background-color: #FFD700;"  
            "border-style: outset;"
            "border-radius: 10px;"
            "border-width: 2px;"
            "border-color: #FFFFE0;"
            "color: black;"  
            "font: bold 14px;"
            "padding: 6px;"
            "}"
            "QPushButton:hover {"
            "background-color: #FFFF00;"  
            "}"
        )
        self.clicked.connect(self.close_application)

    def close_application(self):
        QApplication.instance().quit()