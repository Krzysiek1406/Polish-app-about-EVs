from Pakiet_interfejsu.interfejs import *
from tkinter import filedialog
from matplotlib.backends.backend_pdf import PdfPages


class Eksport_dane_wykres(inter_eksp_dane):
    def __init__(self):
        super().__init__()

    def eksp_dane(self, canva):
        try:
            nazwa_pliku = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Pliki PDF", "*.pdf")])
            if nazwa_pliku:
                with PdfPages(nazwa_pliku) as pdf:
                    pdf.savefig(canva.figure)
        except Exception as e:
            print("Wystąpił błąd:", e)
