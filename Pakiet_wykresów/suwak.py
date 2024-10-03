from PyQt6.QtWidgets import QSlider
from PyQt6.QtCore import Qt


class SliderWidget(QSlider):
    def __init__(self, label_rok, minimum=2013, maximum=2022, value=2018, parent=None):
        super().__init__(Qt.Orientation.Horizontal)
        self.setMinimum(minimum)
        self.setMaximum(maximum)
        self.setValue(value)
        self.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.setTickInterval(1)
        self.label_rok = label_rok
        self.parent = parent
        self.valueChanged.connect(self.update_label)

    def update_label(self, wartosc):
        self.label_rok.update_label(wartosc)
