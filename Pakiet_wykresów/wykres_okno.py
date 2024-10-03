from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, \
    QLineEdit, QHBoxLayout
from PyQt6.QtGui import *
import sys
from Pakiet_wykresów.import_dane_wykres import Import_dane_wykres_przycisk
from Pakiet_wykresów.eksport_dane_wykres import Eksport_dane_wykres
from Pakiet_wykresów.wykres import MplCanvas, LabelRok
from Pakiet_wykresów.lista_państw import Przycisk_panstwa
from Pakiet_wykresów.suwak import SliderWidget
from Pakiet_wykresów.zamykanie import Zamykacz


class wykres(QWidget):
    def __init__(self):
        super().__init__()
        available_geometry = QGuiApplication.primaryScreen().availableGeometry()
        screen_width = available_geometry.width()
        screen_height = available_geometry.height()
        self.proporcja_szerokosci = 1 #screen_width / 2560
        self.proporcja_wysokosci = 1 #screen_height / 1440

        self.resize(int(2560 * self.proporcja_szerokosci), int(1440 * self.proporcja_wysokosci))
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.buttons_clicked = []
        self.przyciski = []
        self.colors = ['purple', 'red', 'lightgreen', 'black', 'yellow', 'orange']
        self.layout = QGridLayout()
        self.layout_przycisków = QGridLayout()
        self.main_layout = QHBoxLayout()
        self.main_layout.addLayout(self.layout,3)
        self.setLayout(self.main_layout)
        self.wykres_do_eksportu = Eksport_dane_wykres()

        self.słownik_państw = {}
        self.btn_import = Import_dane_wykres_przycisk(self.słownik_państw, parent=self)
        self.btn_import.setMaximumWidth(int(500 * self.proporcja_szerokosci))
        self.btn_import.setMinimumWidth(int(400 * self.proporcja_szerokosci))
        self.btn_import.setMinimumHeight(int(100 * self.proporcja_wysokosci))
        self.btn_import.setStyleSheet(
            "QPushButton {"
            "background-color: #007bff;"
            "border-style: outset;"
            "border-radius: 10px;"
            "border-width: 2px;"
            "border-color: #00BFFF;"
            "color: white;"
            "font: bold 14px;"
            "padding: 6px;"
            "}"
            "QPushButton:hover {"
            "background-color: #0056b3;"
            "}"
            )
        self.layout.addWidget(self.btn_import, 0, 0)
        self.btn_import.setDefault(True)

        self.btn_eksport = QPushButton('Eksport')
        self.btn_eksport.setMaximumWidth(int(1100 * self.proporcja_szerokosci))
        self.btn_eksport.setMinimumWidth(int(1100 * self.proporcja_szerokosci))
        self.btn_eksport.setStyleSheet(
            "QPushButton {"
            "background-color: #d32f2f;"
            "border-style: outset;"
            "border-radius: 10px;"
            "border-width: 2px;"
            "border-color: #FFA07A;"
            "color: white;"
            "font: bold 14px;"
            "padding: 6px;"
            "}"
            "QPushButton:hover {"
            "background-color: #8B0000;"
            "}"
            )
        self.btn_eksport.clicked.connect(lambda: self.wykres_do_eksportu.eksp_dane(self.canvas))

        self.zamek = Zamykacz()
        self.zamek.setMaximumWidth(int(500 * self.proporcja_szerokosci))
        self.zamek.setMinimumWidth(int(200 * self.proporcja_szerokosci))
        self.zamek.setMinimumHeight(int(100 * self.proporcja_wysokosci))
        self.layout.addWidget(self.zamek, 0, 2, 1, 1)

        self.label_min_widget = QGridLayout()
        self.label_max_widget = QGridLayout()

        self.label_min = LabelRok(value=2014)
        self.slider_min = SliderWidget(self.label_min, value=2014, parent=self)
        self.change_slider_min
        self.slider_min.valueChanged.connect(self.change_slider_min)

        self.label_max = LabelRok(value=2021)
        self.slider_max = SliderWidget(self.label_max, value=2021, parent=self)
        self.change_slider_max
        self.slider_max.valueChanged.connect(self.change_slider_max)


    def setup_kraje_buttons(self):
        kol = 0
        wiersz = 1
        for country in self.słownik_państw:
            button = Przycisk_panstwa(country, self.buttons_clicked, self, parent=self)
            self.przyciski.append(button)
            if wiersz >= 14:
                kol += 1
                wiersz = 1
            button.setFixedSize(int(100 * self.proporcja_szerokosci), int(58 * self.proporcja_wysokosci))
            if wiersz == 1:
                self.layout_przycisków.addWidget(button, wiersz, kol, 2, 1)
            elif wiersz == 2:
                self.layout_przycisków.addWidget(button, wiersz, kol, 2, 1)
            else:
                self.layout_przycisków.addWidget(button, wiersz, kol, 2, 1)
            wiersz += 1


    def filter_buttons(self):
        filter_text = self.filter_line_edit.text().lower()
        for button in self.przyciski:
            if filter_text in button.text().lower():
                button.show()
            else:
                button.hide()

    def check_sliders_min(self):
        min_value = self.slider_min.value()
        max_value = self.slider_max.value()

        if min_value + 1 > max_value:
            self.slider_min.setValue(max_value)

    def check_sliders_max(self):
        min_value = self.slider_min.value()
        max_value = self.slider_max.value()

        if max_value < min_value + 1:
            self.slider_max.setValue(min_value)

    def update_x_range(self):
        min_value = self.slider_min.value()
        max_value = self.slider_max.value()
        self.canvas.axes.set_xlim(min_value, max_value)
        self.canvas.draw()

    def change_slider_min(self):
        self.check_sliders_min()
        self.update_x_range()
        self.rysuj_wykres()

    def change_slider_max(self):
        self.check_sliders_max()
        self.update_x_range()
        self.rysuj_w

    def change_slider_max(self):
        self.check_sliders_max()
        self.update_x_range()
        self.rysuj_wykres()

    def optimise_buttons(self):
        self.layout.removeWidget(self.zamek)
        self.btn_import.setMaximumWidth(int(1100 * self.proporcja_szerokosci))
        self.btn_import.setMinimumWidth(int(1100 * self.proporcja_szerokosci))
        self.btn_import.setMinimumHeight(10)
        self.zamek.setMaximumWidth(int(1200 * self.proporcja_szerokosci))
        self.zamek.setMinimumWidth(int(300 * self.proporcja_szerokosci))
        self.zamek.setMinimumHeight(10)
        self.filter_line_edit = QLineEdit(self)
        self.filter_line_edit.setPlaceholderText("Szukaj:")
        self.filter_line_edit.textChanged.connect(self.filter_buttons)
        self.layout_przycisków.addWidget(self.filter_line_edit, 1, 0, 1, 3)
        self.layout_przycisków.addWidget(self.zamek, 0, 0, 1, 3)

    def wyswietlanie(self):
        self.rysuj_wykres()

    def rysuj_wykres(self):
        if self.słownik_państw != 0:
            self.optimise_buttons()
            self.layout.addWidget(self.canvas, 2, 0, 20, 2)
            self.layout.addWidget(self.btn_eksport, 0, 1, 1, 1)
            self.label_min_widget.addWidget(self.slider_min, 0, 0, 1, 1)
            self.label_min_widget.addWidget(self.label_min, 1, 0)
            self.label_max_widget.addWidget(self.slider_max, 0, 1, 1, 1)
            self.label_max_widget.addWidget(self.label_max, 1, 1)
            self.layout.addLayout(self.label_min_widget, 23, 0, 1, 1)
            self.layout.addLayout(self.label_max_widget, 23, 1, 1, 1)
            # self.layout.addWidget(self.slider_min,23,0,1,1)
            # self.layout.addWidget(self.label_min,24,0,1,1)
            # self.layout.addWidget(self.slider_max,23,1,1,1)
            # self.layout.addWidget(self.label_max,24,1,1,1)
            self.main_layout.addLayout(self.layout_przycisków, 1)

            self.canvas.clear_plot()
            bar_width = 0.1
            num_bars = len(self.buttons_clicked)
            if num_bars == 1:
                positions = [0]
            elif num_bars == 2:
                positions = [-0.15, 0.15]
            elif num_bars == 3:
                positions = [-0.15, 0, 0.15]
            elif num_bars == 4:
                positions = [-0.225, -0.075, 0.075, 0.225]

            all_years = set()

            min_value = self.slider_min.value()
            max_value = self.slider_max.value()

            for idx, item in enumerate(self.buttons_clicked):
                x = []
                y = []
                data = self.słownik_państw[item]
                for year in data:
                    if min_value <= year <= max_value:
                        x.append(year)
                        y.append(data[year])
                        all_years.add(year)
                print(self.colors[idx])
                bar_positions = [i + positions[idx] for i in x]
                bars = self.canvas.axes.bar(bar_positions, y, width=bar_width, color=self.colors[idx], label=item)
                for bar in bars:
                    yval = bar.get_height()
                    self.canvas.axes.legend(loc='upper left')
                    self.canvas.axes.text(
                        bar.get_x() + bar.get_width() / 2, yval * 1.05, f'{int(yval):,}', ha='center', va='bottom',
                        fontsize=10,
                        fontweight='bold', rotation=90)

            self.canvas.axes.set_xticks(sorted(all_years))
            self.canvas.axes.set_xticklabels(sorted(all_years), rotation=45)

            self.canvas.axes.set_title(f'Nowe samochody elektryczne', fontweight='bold', fontsize=20)
            self.canvas.axes.set_xlabel('Rok', fontweight='bold', fontsize=15)
            self.canvas.axes.set_ylabel('Ilość', fontweight='bold', fontsize=15)
            self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = wykres()
    window.showFullScreen()

    sys.exit(app.exec())
