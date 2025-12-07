from enum import Enum

class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Summa:
    def __init__(self, sovelluslogiikka, syote_lukija):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote_lukija = syote_lukija
        self._arvot = []

    def suorita(self):
        self._arvot.append(self._syote_lukija())
        self._sovelluslogiikka.plus(self._arvot[-1])

    def kumoa(self):
        arvo = self._arvot.pop()
        if arvo is not None:
            self._sovelluslogiikka.miinus(arvo)

class Erotus:
    def __init__(self, sovelluslogiikka, syote_lukija):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote_lukija = syote_lukija
        self._arvot = []

    def suorita(self):
        self._arvot.append(self._syote_lukija())
        self._sovelluslogiikka.miinus(self._arvot[-1])

    def kumoa(self):
        arvo = self._arvot.pop()
        if arvo is not None:
            self._sovelluslogiikka.plus(arvo)

class Nollaus:
    def __init__(self, sovelluslogiikka, syote_lukija):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote_lukija = syote_lukija
        self._arvot = []

    def suorita(self):
        self._arvot.append(self._sovelluslogiikka.arvo())
        self._sovelluslogiikka.nollaa()

    def kumoa(self):
        arvo = self._arvot.pop()
        if arvo is not None:
            self._sovelluslogiikka.aseta_arvo(arvo)

class Kumoa:
    def __init__(self, sovelluslogiikka, komento_hakija):
        self._sovelluslogiikka = sovelluslogiikka
        self._komento_hakija = komento_hakija

    def suorita(self):
        edellinen_komento = self._komento_hakija()
        if edellinen_komento is not None:
            edellinen_komento.kumoa()
