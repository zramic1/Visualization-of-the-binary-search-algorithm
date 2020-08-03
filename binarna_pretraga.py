import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QLabel, QPushButton, QApplication


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Binarna pretraga")

        # Dimenzije
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 600

        self.setGeometry(self.left, self.top, self.width, self.height)

        self.elementiNiza = []
        self.label_list = []
        self.brojRedova = 0

        self.pocetniPrikaz()

        # prikaz svih widgeta
        self.show()

    def pocetniPrikaz(self):
        # Labela za unos elemenata
        self.labela = QLabel("Unesite elemente niza: ", self)
        self.labela.move(20, 20)
        self.labela.resize(120, 20)

        # Textbox za unos elemenata
        self.textbox = QLineEdit(self)
        self.textbox.move(140, 20)
        self.textbox.resize(60, 20)

        self.onlyInt = QIntValidator()
        self.textbox.setValidator(self.onlyInt)

        # Dugme za unos elemenata
        self.dodajButton = QPushButton('Dodaj', self)
        self.dodajButton.move(210, 20)
        self.dodajButton.resize(50, 20)
        self.dodajButton.clicked.connect(self.dodavanjeElemenataKlik)

        # Labela za unos trazenog elementa
        self.labela1 = QLabel("Trazeni element je: ", self)
        self.labela1.move(20, 40)
        self.labela1.resize(120, 40)

        # Textbox za unos elemenata
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(140, 50)
        self.textbox1.resize(60, 20)
        self.textbox1.setValidator(self.onlyInt)

        # Dugme za unos trazenog elementa
        self.trazeniDugme = QPushButton('Zapocni', self)
        self.trazeniDugme.move(210, 50)
        self.trazeniDugme.resize(50, 20)
        self.trazeniDugme.clicked.connect(self.trazeniElementKlik)

        # Dugme za brisanje
        self.obrisiDugme = QPushButton('Obrisi', self)
        self.obrisiDugme.move(280, 50)
        self.obrisiDugme.resize(50, 20)
        self.obrisiDugme.clicked.connect(self.obrisiKlik)

        # Pronadjeni element
        self.labela3 = QLabel("Element je pronadjen na poziciji: ", self)
        self.labela3.move(350, 30)
        self.labela3.resize(200, 40)
        self.labela3.setVisible(False)

        # Indeks pronadjenog elementa
        self.labela4 = QLabel("", self)
        self.labela4.move(520, 30)
        self.labela4.resize(40, 40)
        self.labela4.setStyleSheet("border : 1px solid black;background : white;")
        self.labela4.setVisible(False)

        # Prva okrugla labela
        self.labela5 = QLabel("", self)
        self.labela5.setStyleSheet("background:transparent;")
        self.labela5.setVisible(False)
        self.labela5.resize(30, 30)
        self.labela5.setStyleSheet("border: 2px solid orange;border-radius: 20px;min-height: 40px;min-width: 40px;")

        # Druga okrugla labela
        self.labela6 = QLabel("", self)
        self.labela6.setStyleSheet("background:transparent;")
        self.labela6.resize(30, 30)
        self.labela6.setStyleSheet("border: 2px solid orange;border-radius: 20px;min-height: 40px;min-width: 40px;")
        self.labela6.setVisible(False)

    def dodavanjeElemenataKlik(self):
        textboxValue = self.textbox.text()
        if (len(textboxValue) > 0):
            self.elementiNiza.append(int(textboxValue))
            self.prikaziElementeNiza(textboxValue)
        self.textbox.setText("")

    def prikaziElementeNiza(self, textboxValue):
        jednaLabela = QLabel(textboxValue, self)
        jednaLabela.setStyleSheet("border : 1px solid black;background : white;")
        sirina = (int)((self.width - 40) / len(self.elementiNiza))
        if (len(self.label_list) > 10):
            sirina = (int)((self.width - 40) / 10)

        jednaLabela.setAlignment(Qt.AlignCenter)
        self.label_list.append(jednaLabela)
        for i in range(10 * self.brojRedova, len(self.label_list)):
            self.label_list[i].setGeometry(20 + (i % 10) * sirina, 100 + self.brojRedova * 60, sirina, 40)
        for i in range(len(self.label_list)):
            self.label_list[i].setVisible(True)
        for i in range(len(self.label_list)):
            self.label_list[i].setStyleSheet("border : 1px solid black;background : white;")
        self.brojRedova = (int)(len(self.label_list) / 10)

    def trazeniElementKlik(self):
        textboxValue1 = self.textbox1.text()
        if (len(self.elementiNiza) > 0 and textboxValue1 != ""):
            self.trazeniElement = int(textboxValue1)
            self.dodajButton.setEnabled(False)
            self.trazeniDugme.setEnabled(False)
            self.obrisiDugme.setEnabled(False)
            self.animacija()
        else:
            self.textbox1.setText("")

    def obrisiKlik(self):
        for i in range(len(self.label_list)):
            self.label_list[i].setVisible(False)
        self.label_list = []
        self.elementiNiza = []
        self.brojRedova = 0
        self.prikaziSrednji = True
        self.nadjen = False
        self.labela3.setVisible(False)
        self.labela4.setVisible(False)
        self.labela5.setVisible(False)
        self.labela6.setVisible(False)
        self.textbox1.setText("")

    def animacija(self):
        #Obrisi staru animaciju
        self.prikaziSrednji = True
        self.nadjen = False
        self.labela3.setVisible(False)
        self.labela4.setVisible(False)
        self.labela5.setVisible(False)
        self.labela6.setVisible(False)

        self.elementiNiza.sort()
        for i in range(len(self.label_list)):
            self.label_list[i].setText(str(self.elementiNiza[i]))
        self.prikaziSrednji = True
        self.nadjen = False
        self.donji = 0
        self.gornji = len(self.elementiNiza) - 1
        self.s = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.binarnaPretraga)
        self.timer.start(1500)

    def binarnaPretraga(self):
        if self.donji <= self.gornji:
            if (self.prikaziSrednji):
                self.s = (self.donji + self.gornji) // 2

                self.labela5.move(self.label_list[self.donji].geometry().left() + (int)(
                    (self.label_list[self.donji].geometry().width()) / 2) - 20,
                                  self.label_list[self.donji].geometry().top())
                self.labela6.move(self.label_list[self.gornji].geometry().left() + (int)(
                    (self.label_list[self.gornji].geometry().width()) / 2) - 20,
                                  self.label_list[self.gornji].geometry().top())
                self.labela5.raise_()
                self.labela6.raise_()
                self.labela5.setVisible(True)
                self.labela6.setVisible(True)
                self.label_list[self.s].setStyleSheet("border : 1px solid black;background : blue;")
            else:
                if self.elementiNiza[self.s] < self.trazeniElement:
                    for i in range(self.donji, self.s + 1):
                        self.label_list[i].setStyleSheet("border : 1px solid black;background : red;")
                    self.donji = self.s + 1

                elif self.elementiNiza[self.s] > self.trazeniElement:
                    for i in range(self.s, self.gornji + 1):
                        self.label_list[i].setStyleSheet("border : 1px solid black;background : red;")
                    self.gornji = self.s - 1
                else:
                    self.label_list[self.s].setStyleSheet("border : 1px solid black;background : green;")
                    self.labela4.setText(str(self.s))
                    self.labela4.setAlignment(Qt.AlignCenter)
                    self.labela3.setVisible(True)
                    self.labela4.setVisible(True)
                    self.labela5.setVisible(False)
                    self.labela6.setVisible(False)
                    self.dodajButton.setEnabled(True)
                    self.trazeniDugme.setEnabled(True)
                    self.obrisiDugme.setEnabled(True)
                    self.timer.stop()
            self.prikaziSrednji = not self.prikaziSrednji
        else:
            self.labela3.setText("Element nije pronadjen u nizu!")
            self.labela3.setVisible(True)
            self.labela5.setVisible(False)
            self.labela6.setVisible(False)
            self.dodajButton.setEnabled(True)
            self.trazeniDugme.setEnabled(True)
            self.obrisiDugme.setEnabled(True)
            self.timer.stop()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
