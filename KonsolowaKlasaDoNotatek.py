################################################
# klasa: Notatka
# opis: klasa posiada konstruktor oraz dwie metody,
#       które są odowiedzialne za wyświetlanie tytułu
#       oraz treści notatek i metoda diagnostyczna,
#       która weryfikuje działanie klasy
# pola: licznik_notatek - przechowuje ilość notatek
#       id - unikalny identyfikator każdej notatki
#       tytul_notatki - przechowuje tytuł notatki
#       tresc_notatki - przechowuje treść notatki
# autor: 00000000000
################################################

class Notatka:
    __licznik_notatek = 0
    __id = 0
    _tytul_notatki = ""
    _tresc_notatki = ""

    def __init__(self, _tytul_notatki, _tresc_notatki):
        Notatka.__licznik_notatek += 1
        Notatka.__id = self.__licznik_notatek
        self._tytul_notatki = _tytul_notatki
        self._tresc_notatki = _tresc_notatki

    def wyswietl_tytul_tresc_notatki(self):
        print(self._tytul_notatki, self._tresc_notatki)

    def metoda_diagnostyczna(self):
        print(self.__licznik_notatek , ";" , self.__id , ";" , self._tytul_notatki , ";" , self._tresc_notatki)

notatka1 = Notatka("tytul1", "tresc1")
notatka1.wyswietl_tytul_tresc_notatki()
notatka1.metoda_diagnostyczna()

notatka2 = Notatka("tytul2", "tresc2")
notatka2.wyswietl_tytul_tresc_notatki()
notatka2.metoda_diagnostyczna()