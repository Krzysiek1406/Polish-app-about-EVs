from PyQt6.QtWidgets import QPushButton, QFileDialog, QMessageBox

class Magazyn_danych:
    def __init__(self):
        self.panstwa= []

class Import_mapa_przycisk(QPushButton):
    def __init__(self, DANE):
        super().__init__('Importuj dane txt')
        self.DANE = DANE
        self.setStyleSheet(
            "QPushButton {"
            "background-color: #007bff;"
            "border-style: outset;"
            "border-radius: 10px;"
            "border-width: 2px;"
            "border-color: #0056b3;"
            "color: white;"
            "font: bold 14px;"
            "padding: 6px;"
            "}"
            "QPushButton:hover {"
            "background-color: #0056b3;"
            "}"
        )
        self.clicked.connect(self.otworz_plik)
        self.otworz_plik()


    def utworz_koordynacje(self, file_path):
        # try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(" ")
                lat, lon, *label = parts
                new_label = " ".join(label)
                new_cor = (lat, lon, new_label.strip())
                self.DANE.panstwa.append(new_cor)

        QMessageBox.information(self, "Sukces", "Dane zostały pomyślnie zaimportowane.")


    def otworz_plik(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Wybierz plik", "", "Text Files (*.txt);;All Files (*)")

        if file_path:
            self.utworz_koordynacje(file_path)
        else:
            self.gdy_error()

    def gdy_error(self):
        response = QMessageBox.question(self, "Błąd", "Nieodpowiedni plik. Czy chcesz wczytać inny plik?",
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                        defaultButton=QMessageBox.StandardButton.Yes)
        if response == QMessageBox.StandardButton.Yes:
            self.otworz_plik()
        else:
            QMessageBox.warning(self, "Uwaga", "Nie udało się wczytać danych.")



