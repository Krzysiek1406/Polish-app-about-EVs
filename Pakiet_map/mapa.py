import folium
from PyQt6 import QtWidgets, QtWebEngineWidgets
from PyQt6.QtWidgets import QApplication, QWidget
import sys
from Pakiet_map.import_dane_mapa_przycisk import Import_mapa_przycisk, Magazyn_danych


class Mapa(QWidget):
    def __init__(self, DATATA):
        super().__init__()
        self.datata = DATATA
        self.__marker_group = folium.FeatureGroup()
        self.mapa = folium.Map(location=[52.2297, 21.0122], zoom_start=6)
        self.forek()


    def forek(self):
        for stacja_ladowania in self.datata.panstwa[2000:]:
            x,y,nazwa = stacja_ladowania
            self.dodaj_punkt(x, y, nazwa)

    def dodaj_punkt(self, lat, lon, name):
        marker = folium.Marker(location=[lat, lon], popup=name)
        self.__marker_group.add_child(marker)
        self.mapa.add_child(self.__marker_group)

    def pobierz_html(self):
        return self.mapa.get_root().render()


class Obsluga_mapy(QtWidgets.QWidget):
    def __init__(self, widget_main, DATATA):
        super().__init__()
        self.DATATA = DATATA
        self.widget_main = widget_main

        layout_teksty = QtWidgets.QHBoxLayout()
        layout_przyciski = QtWidgets.QHBoxLayout()

        self.cor_x = QtWidgets.QLineEdit(self)
        self.cor_x.setPlaceholderText("Podaj cor x:")

        self.cor_y = QtWidgets.QLineEdit(self)
        self.cor_y.setPlaceholderText("Podaj cor y:")

        self.nazwa = QtWidgets.QLineEdit(self)
        self.nazwa.setPlaceholderText("Podaj nazwe:")

        layout_teksty.addWidget(self.cor_x)
        layout_teksty.addWidget(self.cor_y)
        layout_teksty.addWidget(self.nazwa)

        self.dodawanie_przycisk = QtWidgets.QPushButton('Dodaj stacje', self)
        self.dodawanie_przycisk.clicked.connect(self.dodaj_stacje)

        self.usuwanie_przycisk = QtWidgets.QPushButton('Usun stacje', self)
        self.usuwanie_przycisk.clicked.connect(self.usun_stacje)

        layout_przyciski.addWidget(self.dodawanie_przycisk)
        layout_przyciski.addWidget(self.usuwanie_przycisk)

        layout_glowny = QtWidgets.QVBoxLayout()
        layout_glowny.addLayout(layout_teksty)
        layout_glowny.addLayout(layout_przyciski)

        self.setLayout(layout_glowny)

    def dodaj_stacje(self):
        ladowarka = (self.cor_x.text(), self.cor_y.text(), self.nazwa.text())
        if ladowarka not in self.DATATA.panstwa:
            self.DATATA.panstwa.append(ladowarka)
            self.widget_main.przeladuj_mape()

    def usun_stacje(self):
        ladowarka = (self.cor_x.text(), self.cor_y.text(), self.nazwa.text())
        if ladowarka in self.DATATA.panstwa:
            self.DATATA.panstwa.remove(ladowarka)
            self.widget_main.przeladuj_mape()



class Mapa_okno(QtWidgets.QWidget):
    def __init__(self, DATATA):
        super().__init__()
        self.DATATA = DATATA
        self.mapa = Mapa(DATATA)

        self.widok_mapa = QtWebEngineWidgets.QWebEngineView()
        self.widok_mapa.setHtml(self.mapa.pobierz_html())
        self.przyciski = Obsluga_mapy(self, self.DATATA)

        layout_mapa = QtWidgets.QGridLayout()
        layout_mapa.addWidget(self.widok_mapa, 0, 0, 5, 0)
        layout_mapa.addWidget(self.przyciski, 6, 0)
        self.setLayout(layout_mapa)

    def przeladuj_mape(self):
        self.mapa = Mapa(self.DATATA)
        new_html = self.mapa.pobierz_html()
        self.widok_mapa.setHtml(new_html)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    Dane = Magazyn_danych()
    importowarka = Import_mapa_przycisk(Dane)
    Okno = Mapa_okno(Dane)


    Okno.showFullScreen()
    sys.exit(app.exec())