import sys
import requests

from PyQt5.QtWidgets import QWidget,QAction,QApplication,QLineEdit,QLabel,QPushButton,QVBoxLayout,qApp,QMainWindow,QFileDialog,QHBoxLayout


class pencere(QWidget):

    def __init__(self):
        super().__init__()

        self. init_ui()

    def init_ui(self):
        self.birinci_döviz=QLineEdit()
        self.ikinci_döviz=QLineEdit()
        self.miktar=QLineEdit()
        self.temizle =QPushButton("Temizle")
        self.hesapla=QPushButton("hesapla")
        self.hesaplanan=QLineEdit()

        h_box=QHBoxLayout()
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.hesapla)

        v_box = QVBoxLayout()

        v_box.addWidget(self.birinci_döviz)
        v_box.addWidget(self.ikinci_döviz)
        v_box.addWidget(self.miktar)
        v_box.addWidget(self.hesaplanan)

        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.setWindowTitle("pencere")

        self.temizle.clicked.connect(self.yazi_temizle)
        self.hesapla.clicked.connect(self.hesaplama)

        self.show()

    def yazi_temizle(self):
        self.birinci_döviz.clear()
        self.ikinci_döviz.clear()
        self.miktar.clear()
        self.hesaplanan.clear()

        
    def hesaplama(self):
        url ="https://canlidoviz.com/doviz-kurlari/kapali-carsi"

        birinci_döviz = self.birinci_döviz.text()
        ikinci_döviz = self.ikinci_döviz.text()
        miktar = float(self.miktar.text())

        response = requests.get(url + birinci_döviz)
    
        if response.status_code == 200:
            html_content = response.text

            start_index = html_content.find('<table class="table-detail">') + len('<table class="table-detail">')
            end_index = html_content.find('</table>', start_index)
            exchange_rate_str = html_content[start_index:end_index]
        try:
            exchange_rate = float(exchange_rate_str.replace(",", ""))
        except ValueError:
            print("Failed to parse exchange rate.")
            return

 
        birinci_doviz = self.birinci_doviz.text()
        ikinci_doviz = self.ikinci_doviz.text()
        miktar = float(self.miktar.text())

           
        converted_amount = exchange_rate * miktar

        print(f"{miktar} {birinci_doviz} is equal to {converted_amount} {ikinci_doviz}")



app = QApplication(sys.argv)

pencere=pencere()

sys.exit(app.exec_())