import sys
import requests
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QComboBox,QVBoxLayout,QPushButton,QSizePolicy
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import Qt

class Anime_character(QWidget):
    def __init__(self):
        super().__init__()
        self.heading=QLabel('Anime Character')
        self.combo_box = QComboBox()
        self.characters=[
    "Naruto","Sasuke","Itachi","Luffy","Zoro",
    "Gojo","Goku","Levi","Eren","Mikasa","Light Yagami","L Lawliet","Tanjiro","Nezuko","Killua",
    "Gon","Kakashi","Madara","Saitama","Edward Elric"]
        self.combo_box.addItems(self.characters)
        self.get_image_button=QPushButton('Get Image',self)
        self.image_label=QLabel(self)
        self.detail_label=QLabel(self)
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Anime Character')
        self.setGeometry(300, 300, 250, 150)

        vbox=QVBoxLayout()

        self.heading.setAlignment(Qt.AlignCenter)
        self.heading.setStyleSheet("font-size: 30px; font-weight: bold;")
        vbox.addWidget(self.heading)

        self.combo_box.setStyleSheet("font-size: 50px;"
                                     " font-weight: bold;"
                                     "background-color:#ff2692;")
        self.combo_box.setFixedWidth(800)
        vbox.addWidget(self.combo_box,alignment=Qt.AlignCenter)


        self.get_image_button.setFixedWidth(400)
        self.get_image_button.setObjectName('get_image_button')
        vbox.addWidget(self.get_image_button, alignment=Qt.AlignHCenter)


        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(300, 300)
        vbox.addWidget(self.image_label, alignment=Qt.AlignCenter)


        self.detail_label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.detail_label)
        self.detail_label.setStyleSheet("font-size: 20px;"
                                        "font-family: Arial;")


        self.setLayout(vbox)

        self.detail_label.setWordWrap(True)


        self.get_image_button.setObjectName('get_image_button')

        self.setStyleSheet('''
        QWidget {
        background-color:rgb(73, 157, 203);
        }
        #get_image_button {
        background-color:#ff2692;
        padding:15;
        border-radius:15px;
        }
        ''')

        self.get_image_button.setFixedWidth(200)
        self.get_image_button.setSizePolicy(
            QSizePolicy.Fixed,
            QSizePolicy.Fixed
        )

        self.get_image_button.clicked.connect(self.get_image)
    def get_image(self):
        choice=self.combo_box.currentText()
        url=f"https://api.jikan.moe/v4/characters?q={choice}"

        response=requests.get(url)
        try:
            response.raise_for_status()
            if response.status_code==200:
                data = response.json()
                image_url = data["data"][0]["images"]["jpg"]["image_url"]

                char=data['data'][0]

                name=char.get("name","No Name")
                about=char.get('about','No Description')
                if about:
                    about=about[:300]+"..."

                kanji = char.get("name_kanji","N/A")


                image_data=requests.get(image_url).content

                pixmap=QPixmap()
                pixmap.loadFromData(image_data)

                self.image_label.setPixmap(pixmap.scaled(300,300,Qt.KeepAspectRatio))

                self.detail_label.setText(f"Name:{name}\nKanji:{kanji}\nAbout:{about}")

        except requests.exceptions.ConnectionError:
            self.display_error('connection error\nPlease check your internet connection')
        except requests.exceptions.Timeout:
            self.display_error('timed out error\nThe requested timed out')
        except requests.exceptions.TooManyRedirects:
            self.display_error('too many redirects error\nCheck the URL')
        except requests.exceptions.RequestException as req_error:
            self.display_error(f'request error occured:\n{req_error}')

    def display_error(self, message):
        self.image_label.setStyleSheet('font-size:30px')
        self.image_label.setText(message)


if __name__=='__main__':
    app=QApplication(sys.argv)
    anime_character=Anime_character()
    anime_character.show()
    sys.exit(app.exec_())

