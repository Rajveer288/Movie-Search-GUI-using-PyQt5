import sys

import requests
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QLayout, QComboBox
from PyQt5.QtCore import Qt

class CurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.button_converter=QPushButton("Convert",self)
        self.currencies=["USD","INR","EUR","GBP","JPY","CNY","CAD","AUD","CHF","SGD","HKD"]
        self.from_currency=QComboBox()
        self.to_currency=QComboBox()
        self.result_label=QLabel('-----RESULT-----',self)
        self.line_edit_amount=QLineEdit(self)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Currency Converter")
        self.setGeometry(700, 300, 600, 600)
        self.line_edit_amount.setPlaceholderText("Enter Amount")
        self.from_currency.addItems(self.currencies)
        self.to_currency.addItems(self.currencies)

        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addWidget(self.line_edit_amount)
        vbox.addWidget(self.from_currency)
        vbox.addWidget(self.to_currency)
        vbox.addWidget(self.button_converter)
        vbox.addWidget(self.result_label)
        self.setLayout(vbox)
        vbox.addStretch()
        vbox.setSpacing(15)

        self.line_edit_amount.setAlignment(Qt.AlignCenter)
        self.result_label.setAlignment(Qt.AlignCenter)

        self.setStyleSheet('''
        QWidget {
        background-color: rgb(128,128,128);
        }
        QComboBox {
        padding: 5px;
        font-size: 25px;
        font-style: Arial;
        }
        QLineEdit,QPushButton {
        padding: 19px;
        font-size: 25px;
        font-weight: bold;
        font-style: Arial;
        }
        QLabel{
        padding: 10px;
        font-size: 30px;
        font-style: Arial;
        font-weight: bold;
        }
        ''')
        self.button_converter.clicked.connect(self.button_on_click)

    def button_on_click(self):
        try:
            amount=float(self.line_edit_amount.text())
            from_currency=self.from_currency.currentText()
            to_currency=self.to_currency.currentText()

            if not amount:
                self.result_label.setText("Enter Amount")
                return
            url=f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"

            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            result=data['rates'][to_currency]
            self.result_label.setText(f"{result}{to_currency}")

        except ValueError:
            self.display_error('Invalid Input')

        except requests.exceptions.ConnectionError:
            self.display_error('connection error\nPlease check your internet connection')
        except requests.exceptions.Timeout:
            self.display_error('timed out error\nThe requested timed out')
        except requests.exceptions.TooManyRedirects:
            self.display_error('too many redirects error\nCheck the URL')
        except requests.exceptions.RequestException as req_error:
            self.display_error(f'request error occured:\n{req_error}')
        except requests.exceptions.HTTPError as http_error:
            self.display_error(f'request error occured:\n{http_error}')
    def display_error(self,message):
        self.result_label.setStyleSheet('font-size:30px;'
                                        'font-style: Arial;'
                                        'font-weight: bold;')
        self.result_label.setText(message)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    currency = CurrencyConverter()
    currency.show()
    sys.exit(app.exec_())