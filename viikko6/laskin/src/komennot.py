from enum import Enum

class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Summa:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka

    def suorita(self, syote):
        self._sovelluslogiikka.plus(syote)

class Erotus:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka

    def suorita(self, syote):
        self._sovelluslogiikka.miinus(syote)

class Nollaus:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka

    def suorita(self, syote = None):
        self._sovelluslogiikka.nollaa()
