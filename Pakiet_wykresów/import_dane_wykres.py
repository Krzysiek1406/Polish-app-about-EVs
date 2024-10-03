from Pakiet_interfejsu.interfejs import *
import pandas as pd
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox
import sys
from tkinter import filedialog


class Import_dane_wykres(inter_wczyt_dane):
    def __init__(self, file_path, sheet_name='Sheet 1', start_row=8, end_row=48, start_col=0, end_col=20):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.start_row = start_row
        self.end_row = end_row
        self.start_col = start_col
        self.end_col = end_col
        self.data_dict = {}
        self.rows, self.columns = 0, 0
        self.array = self.wczyt_dane()

    def pokaz(self):
        df = pd.DataFrame(self.array)
        print(df)

    def set_dict(self):
        self.rows = len(self.array)
        self.columns = len(self.array[0])  # zmienione z self.array.columns

        for c in range(1, self.rows):
            country = self.array[c][0]
            years_data = {}
            for col in range(1, self.columns):
                year = int(self.array[0][col])
                new_data = int(self.array[c][col])
                years_data[year] = new_data
            self.data_dict[country] = years_data

    def get_dict(self):
        return self.data_dict

    def wczyt_dane(self):
        try:
            data2 = pd.read_excel(self.file_path, self.sheet_name, header=None,
                                  usecols=range(self.start_col, self.end_col + 1),
                                  nrows=self.end_row - self.start_row + 1, skiprows=self.start_row)
            data2 = data2.values.tolist()
            data2 = self.kondycjonowanie(data2)
            print('Plik wczytany pomyślnie')
            return data2
        except Exception as e:
            print("Błąd wczytywania danych:", e)
            return None

    def get_dane(self):
        return self.array

    def kondycjonowanie(self, data):
        df = pd.DataFrame(data)
        df = df.drop(df.columns[2::2], axis=1)
        df = df.fillna(':')
        df = df.replace(to_replace=':', value=0)
        df = df.drop(index=1)
        array_cleaned = df.values.tolist()
        return array_cleaned


class Import_dane_wykres_przycisk(QPushButton):
    def __init__(self, słownik, parent=None):
        super().__init__('Importuj dane Excel', parent)
        self.dane_wykres = None
        self.clicked.connect(self.click)
        self.parent = parent
        self.dict = {}
        self.słownik = słownik

    def click(self):
        file_path = filedialog.askopenfilename(filetypes=(("xlsx", ".xlsx"), ("all files", ".*")))

        if file_path:
            self.dane_wykres = Import_dane_wykres(file_path)
            if self.dane_wykres.array is not None:
                self.dane_wykres.pokaz()
                self.dane_wykres.set_dict()
                self.dict = self.dane_wykres.get_dict()
                self.słownik.update(self.dict)

                if self.parent:
                    self.parent.setup_kraje_buttons()
                    self.parent.wyswietlanie()
            else:
                self.gdy_error()

        else:
            print('Nie wybrano pliku')

    def gdy_error(self):
        response = QMessageBox.question(self, "Błąd", "Nieodpowiedni plik. Czy chcesz wczytać inny plik?",
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                        defaultButton=QMessageBox.StandardButton.Yes)
        if response == QMessageBox.StandardButton.Yes:
            self.click()
        else:
            print('Nie udało się wczytać danych')

    def pokaz(self):
        if self.dane_wykres:
            self.dane_wykres.pokaz()
        else:
            print('Dane nie zostały wczytane')


class Import_dane_wykres_okno(QWidget):
    def __init__(self, słownik):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.przycisk = Import_dane_wykres_przycisk(słownik)

        layout.addWidget(self.przycisk)


if __name__ == "__main__":
    słownik = {}
    app = QApplication(sys.argv)
    window = Import_dane_wykres_okno(słownik)
    window.show()

    sys.exit(app.exec())
