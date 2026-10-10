import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton, QVBoxLayout, QWidget,QGridLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class CalculatorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon(r'20260216_OHR.JorvikVikingFestival2026_EN-GB0705464256_UHD_bing.jpg'))
        self.button_1 = QPushButton('1',self)
        self.button_2 = QPushButton('2',self)
        self.button_3 = QPushButton('3',self)
        self.button_4 = QPushButton('4',self)
        self.button_5 = QPushButton('5',self)
        self.button_6 = QPushButton('6',self)
        self.button_7 = QPushButton('7',self)
        self.button_8 = QPushButton('8',self)
        self.button_9 = QPushButton('9',self)
        self.clear_button=QPushButton('Clear',self)
        self.addition_button=QPushButton("+",self)
        self.subtraction_button=QPushButton("-",self)
        self.multiplication_button=QPushButton("*",self)
        self.division_button=QPushButton("/",self)
        self.equal_button=QPushButton("=",self)
        self.dot_button=QPushButton(".",self)
        self.zero_button=QPushButton("0",self)

        self.linedit=QLineEdit(self)
        self.setGeometry(500,200,800,700)
        self.initUI()

    def initUI(self):
        self.linedit.setPlaceholderText('Enter number here')
        vbox = QVBoxLayout()
        grid = QGridLayout()

        grid.addWidget(self.button_1,2,1)
        grid.addWidget(self.button_2,2,2)
        grid.addWidget(self.button_3,2,3)
        grid.addWidget(self.button_4,3,1)
        grid.addWidget(self.button_5,3,2)
        grid.addWidget(self.button_6,3,3)
        grid.addWidget(self.button_7,4,1)
        grid.addWidget(self.button_8,4,2)
        grid.addWidget(self.button_9,4,3)
        grid.addWidget(self.addition_button,2,4)
        grid.addWidget(self.subtraction_button,3,4)
        grid.addWidget(self.multiplication_button,4,4)
        grid.addWidget(self.division_button,5,4)
        grid.addWidget(self.linedit,1,1,3,4)
        grid.addWidget(self.equal_button,5,3)
        grid.addWidget(self.dot_button,5,2)
        grid.addWidget(self.zero_button,5,1)
        grid.addWidget(self.clear_button,6,4)


        vbox.addLayout(grid)
        self.setLayout(vbox)

        self.setStyleSheet('''
        QWidget{
        background-color: rgb(34, 192, 245);
        }
        QPushButton {
        background-color: rgb(228, 235, 40);
        font-weight: bold;
        font-size: 40px;
        font-family:Arial;
        border-radius: 20px;
        }
        QPushButton:hover {
        background-color: rgb(242, 146, 19);
        }
        QLineEdit {
        font-size: 60px;
        padding: 10px;
        }
        ''')
        self.buttons=[
            self.button_1,self.button_2,self.button_3,self.button_4,self.button_5,
            self.button_6,self.button_7,self.button_8,self.button_9,self.zero_button
        ]
        for button in self.buttons:
            button.clicked.connect(lambda:self.button_clicked())
        self.operators=[
            self.addition_button,self.subtraction_button,self.multiplication_button,self.division_button,
            self.equal_button,self.dot_button
        ]
        for operator in self.operators:
            operator.clicked.connect(lambda:self.button_clicked())

        self.clear_button.clicked.connect(self.clear)

    def button_clicked(self):
        signal=self.sender()
        read=signal.text()
        current=self.linedit.text()
        operators='+-*/'

        if read=='=':
            if current=="":
                return
            try:
                result=eval(self.linedit.text())
                self.linedit.setText(str(result))
            except:
                self.linedit.setText('Invalid Input')
            return
        else:
            if current=="" and read in operators:
                return
            if current and current[-1] in operators and read in operators:
                self.linedit.setText(current[:-1] + read)
                return
            self.linedit.setText(self.linedit.text()+read)
    def clear(self):
        self.linedit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Calculator=CalculatorWindow()
    Calculator.show()
    sys.exit(app.exec_())