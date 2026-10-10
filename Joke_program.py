import requests
import random
import sys
from PyQt5.QtWidgets import QApplication,QLabel,QPushButton,QVBoxLayout,QWidget,QHBoxLayout
from PyQt5.QtCore import Qt

class Joke(QWidget):
    def __init__(self):
        super().__init__()
        self.show_button = QPushButton("Show Joke")
        self.choices = ["😂", "🤣", "😆", "😄", "😹","😜", "😝", "🤪", "😛","😹", "😸", "😁","😎", "🥳", "🤭"]
        self.setGeometry(650, 300, 800, 500)
        self.setWindowTitle("Joke Generator 😂")
        self.remove_button = QPushButton("Remove Joke")
        self.label_setup=QLabel(self)
        self.label_punchline=QLabel(self)
        self.emoji_label=QLabel(self)
        self.dark_mode=QPushButton("🌙",self)
        self.dark=False
        self.initUI()
    def initUI(self):
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.dark_mode)

        vbox=QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.show_button)
        vbox.addWidget(self.remove_button)
        vbox.addWidget(self.label_setup)
        vbox.addWidget(self.label_punchline)
        vbox.addWidget(self.emoji_label)
        self.setLayout(vbox)

        vbox.addLayout(hbox)

        self.label_setup.setAlignment(Qt.AlignCenter)
        self.label_punchline.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)

        self.label_punchline.setObjectName("label_punchline")
        self.emoji_label.setObjectName("emoji_label")
        self.label_setup.setObjectName("label_setup")

        self.setStyleSheet('''
        QWidget{
        background-color:rgb(255, 234, 0);
        }
        QPushButton{
        background-color:rgb(255, 165, 0);
        padding:10px;
        border-radius:10px;
        font-size:20px;
        }
        QLabel#label_setup,QLabel#label_punchline{
        font-size:28px;
        font-family:Arial;
        }
        QLabel#emoji_label{
        font-size:80px;
        }
        ''')

        self.show_button.clicked.connect(self.show_joke)
        self.remove_button.clicked.connect(self.remove_joke)
        self.dark_mode.clicked.connect(self.dark_mode_on)

    def show_joke(self):
        try:
            url = "https://official-joke-api.appspot.com/random_joke"
            response = requests.get(url,timeout=5)
            if response.status_code == 200:
                data=response.json()


                self.label_setup.setText(data["setup"])
                self.label_punchline.setText(data["punchline"])
                self.emoji_label.setText(random.choice(self.choices))
            else:
                self.label_setup.setText("Failed to get joke")
        except requests.exceptions.ConnectionError:
            self.display_error('connection error\nPlease check your internet connection')
        except requests.exceptions.Timeout:
            self.display_error('timed out error\nThe requested timed out')
        except requests.exceptions.TooManyRedirects:
            self.display_error('too many redirects error\nCheck the URL')
        except requests.exceptions.RequestException as req_error:
            self.display_error(f'request error occured:\n{req_error}')
        except Exception:
            self.display_error('unexpected error\nCheck the URL')

    def remove_joke(self):
        self.label_setup.clear()
        self.label_punchline.clear()
        self.emoji_label.clear()
    def display_error(self,message):
        self.label_punchline.setStyleSheet('font-size:28px')
        self.label_punchline.setText(message)
        self.emoji_label.clear()
    def dark_mode_on(self):
        self.show_button.setObjectName('show_button')
        self.remove_button.setObjectName('remove_button')
        self.label_setup.setObjectName("label_setup")

        if not self.dark:
            self.setStyleSheet('''
            QWidget{
            background-color:rgb(30,30,30);
            }
            QPushButton#show_button,QPushButton#remove_button{
            background-color:rgb(255,255,255);
            padding:10px;
            border-radius:10px;
            font-size:20px;
            }
            QLabel#label_setup,QLabel#label_punchline{
            color:rgb(255,255,255);
            font-size:28px;
            font-family:Arial;
            }
            QLabel#emoji_label{
            font-size:80px;
            }
            QPushButton#dark_mode{
            padding:10px;
            border-radius:10px;
            font-size:20px;
            background-color:rgb(255,255,255);
            ''')
            self.dark=True
        else:
            self.setStyleSheet('''
            QWidget{
            background-color:rgb(255, 234, 0);
            }
            QPushButton{
            background-color:rgb(255, 165, 0);
            padding:10px;
            border-radius:10px;
            font-size:20px;
            }
            QLabel#label_setup,QLabel#label_punchline{
            font-size:28px;
            font-family:Arial;
            }
            QLabel#emoji_label{
            font-size:80px;
            }
            ''')

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Joke()
    ex.show()
    sys.exit(app.exec_())