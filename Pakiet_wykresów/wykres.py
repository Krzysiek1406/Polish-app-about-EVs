from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=10, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
        self.axes.spines['top'].set_visible(False)
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['left'].set_visible(True)
        self.axes.spines['bottom'].set_visible(True)


    def clear_plot(self):
        self.axes.cla()
        self.draw()


class LabelRok(QWidget):
    def __init__(self, value=2018):
        super().__init__()
        self.value = value
        self.label = QLabel(f'{self.value}')
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def update_label(self, wartosc):
        self.value = wartosc
        self.label.setText(f'{self.value}')
