from PyQt6.QtWidgets import QPushButton, QMessageBox


class Przycisk_panstwa(QPushButton):
    def __init__(self, country, btn_clicked, wykres, parent=None):
        super().__init__()
        self.setObjectName(country)
        self.btn_clicked = btn_clicked
        self.wykres = wykres
        self.parent = parent
        self.setStyleSheet("background-color: white; color: black")
        self.setText(country)
        self.clicked.connect(self.click)

    def click(self):
        btn = self.parent.sender()
        key = btn.objectName()


        if key in self.btn_clicked:
            self.btn_clicked.remove(key)
            self.wykres.wyswietlanie()
            btn.setStyleSheet("background-color: white; color:black")
        elif key not in self.btn_clicked and len(self.btn_clicked) < 4:
            self.btn_clicked.append(key)
            print(self.btn_clicked)
            btn.setStyleSheet("background-color: lightgreen; color: black")
            self.wykres.wyswietlanie()
        else:
            self.gdy_za_duzo_panstw()

    def gdy_za_duzo_panstw(self):
        response = QMessageBox(self.parent)
        response.setWindowTitle("Błąd")
        response.setText("Maksymalna liczba państw osiągnięta")
        response.setStyleSheet("QMessageBox {text-align: center;}""QPushButton { padding: 10px; }")
        response.setStyleSheet(
            "QMessageBox { background-color: #333333; border: 2px solid #666666; }"
            "QPushButton { padding: 10px; background-color: #333333; color: white; border-radius: 5px; }"
            "QPushButton:hover { background-color: #333333; }"
            )
        ok_button = response.addButton("OK", QMessageBox.ButtonRole.AcceptRole)
        response.setDefaultButton(ok_button)
        response.exec()

