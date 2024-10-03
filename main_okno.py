from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QTabWidget, QGridLayout, \
    QPushButton
import sys
from Pakiet_wykresów.wykres_okno import wykres
from Pakiet_map.mapa import Mapa_okno, Import_mapa_przycisk
from Pakiet_map.import_dane_mapa_przycisk import Magazyn_danych



class Main_okno(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__tab1 = Tab1(self)
        self.__tab2 = Tab2(self)
        self.__tabs = Main_Tab(self.__tab1, self.__tab2)
        dark_stylesheet = """
            QWidget {
                background-color: #1e1e1e;
                color: #f0f0f0;
            }

            QPushButton {
                background-color: #2a2a2a;
                border-style: outset;
                border-radius: 10px;
                border-width: 2px;
                border-color: #1e1e1e;
                color: white;
                font: bold 14px;
                padding: 6px;
            }

            QPushButton:hover {
                background-color: #333333;
            }

            QLabel {
                color: #f0f0f0;
            }

            QSlider::handle:horizontal {
                background-color: #2a2a2a;
                border: 2px solid #1e1e1e;
                width: 18px;
                margin-top: -6px;
                margin-bottom: -6px;
                border-radius: 10px;
            }

            QSlider::groove:horizontal {
                background-color: #1e1e1e;
                height: 8px;
                border-radius: 4px;
            }
        """
        self.setStyleSheet(dark_stylesheet)


class Main_Tab(QTabWidget):
    def __init__(self, tab1, tab2):
        super().__init__()
        self.__tab1 = tab1
        self.__tab2 = tab2
        self.addTab(self.__tab1, 'WYKRES')
        self.addTab(self.__tab2, 'MAPA')
        self.setWindowTitle("Free VBucks = 20 + j15")
        self.showFullScreen()



class Tab1(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QHBoxLayout(self)
        window_wykres = wykres()
        self.layout.addWidget(window_wykres)
        self.setLayout(self.layout)
        self.setWindowTitle("wykres")


class Tab2(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QGridLayout(self)
        self.Dane = Magazyn_danych()

        self.button_wczytaj = QPushButton("WCZYTAJ")
        self.button_wczytaj.setStyleSheet(
            "QPushButton {"
            "background-color: #28a745;"
            "border-style: outset;"
            "border-radius: 10px;"
            "border-width: 2px;"
            "border-color: #7CFC00;"
            "color: white;"
            "font: bold 14px;"
            "padding: 6px;"
            "}"
            "QPushButton:hover {"
            "background-color: #218838;"
            "}"
            )

        self.button_wczytaj.setFixedSize(500, 100)
        self.button_wczytaj.clicked.connect(self.klk)
        self.layout.addWidget(self.button_wczytaj)

    def klk(self):
        importowarkoinator = Import_mapa_przycisk(self.Dane)
        widget_mapa = Mapa_okno(self.Dane)
        self.button_wczytaj.hide()

        self.layout.addWidget(widget_mapa)
        self.setLayout(self.layout)
        self.setWindowTitle("MAPA")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Main_okno()
    sys.exit(app.exec())
