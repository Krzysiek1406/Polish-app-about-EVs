from abc import ABC, abstractmethod


class inter_lista_państw(ABC):
    @abstractmethod
    def wyświetl_listę(self):
        raise "Metoda wyświetl_listę niezaimplementowana"

    @abstractmethod
    def zaznacz_państwo(self):
        raise "Metoda zaznacz_państwo niezaimplementowana"


class inter_wykres(ABC):
    @abstractmethod
    def wyświetlanie(self):
        raise "Metoda wyświetlanie niezaimplementowana"


class inter_wczyt_dane(ABC):
    @abstractmethod
    def wczyt_dane(self):
        raise "Metoda wczyt_dane niezaimplementowana"


class inter_eksp_dane(ABC):
    @abstractmethod
    def eksp_dane(self):
        raise "Metoda eksp_dane niezaimplementowana"
