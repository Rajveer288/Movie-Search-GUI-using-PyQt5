import sys
import requests

from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout,QListWidgetItem,QTextEdit,QListWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class SearchMovie(QWidget):
    def __init__(self):
        super().__init__()
        self.search_bar = QLineEdit(self)
        self.movies_recommendation=QListWidget(self)
        self.search_button=QPushButton("Search",self)
        self.poster = QLabel("Poster: ")
        self.title = QLabel("Title: ")
        self.year = QLabel("Year: ")
        self.genre = QLabel("Genre: ")
        self.rating = QLabel("Rating: ")
        self.plot = QTextEdit()

        self.initUI()
    def initUI(self):
        self.setWindowTitle("Search Movie")
        self.setGeometry(300, 300, 900, 600)

        main_layout = QVBoxLayout()

        search_layout=QHBoxLayout()

        content_layout=QHBoxLayout()

        details_layout=QVBoxLayout()

        details_layout.addWidget(self.poster)
        details_layout.addWidget(self.title)
        details_layout.addWidget(self.year)
        details_layout.addWidget(self.genre)
        details_layout.addWidget(self.rating)
        details_layout.addWidget(self.plot)


        content_layout.addWidget(self.movies_recommendation,1)
        content_layout.addLayout(details_layout,2)

        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(self.search_button)

        main_layout.addLayout(search_layout)
        main_layout.addLayout(content_layout)
        self.setLayout(main_layout)

        self.plot.setReadOnly(True)

        self.setStyleSheet("""
        QWidget {
        background-color: #121212;
        }
        QLineEdit {
        background-color: #1E1E1E;
        color: white;
        border: 2px solid #333333;
        border-radius: 8px;
        padding: 8px;
        }
        QPushButton {
        background-color: #E50914;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 8px 16px;
        }
        QPushButton:hover
        {
        background-color: #F6121D;
        }
        QListWidget {
        background-color: #181818;
        color: white;
        border: 1px solid #333333;
        }
        QListWidget::item {
        padding: 8px;
        }
        QListWidget::item:selected {
        background-color: #E50914;
        color: white;
        }
        """)
        for widget in [self.title,self.year,self.genre,self.rating,self.plot]:
            widget.setStyleSheet("color:white;"
                                 "font-size:16px;")

        self.poster.setFixedSize(250,350)
        self.poster.setAlignment(Qt.AlignCenter)
        self.poster.setStyleSheet("""
            background-color:#1E1E1E;
            border:1px solid #333;
            color:white;
        """)
        content_layout.setSpacing(15)

        self.search_bar.setPlaceholderText("Search for a movie")
        self.plot.setMinimumHeight(250)

        self.search_button.clicked.connect(self.search_movie)

    def search_movie(self):
        movie_name=self.search_bar.text()
        API_KEY="c2ec113b"
        url=f"https://www.omdbapi.com/?apikey={API_KEY}&s={movie_name}"
        try:
            response = requests.get(url)
            response.raise_for_status()

            if response.status_code == 200:
                data=response.json()
                if data.get("Response") == "False":
                    print(data["Error"])
                    return
                self.movies_recommendation.clear()
                for movie in data["Search"]:
                    item=QListWidgetItem(
                        f"{movie['Title']} ({movie['Year']})"
                    )
                    item.setData(Qt.UserRole, movie["imdbID"])
                    self.movies_recommendation.addItem(item)

            self.movies_recommendation.itemClicked.connect(self.show_movie_details)


        except requests.exceptions.ConnectionError:
            self.display_error('connection error\nPlease check your internet connection')
    def show_movie_details(self,item):
        imdb_ID=item.data(Qt.UserRole)
        API_KEY="c2ec113b"
        url_imdb=f"https://www.omdbapi.com/?apikey={API_KEY}&i={imdb_ID}"
        response = requests.get(url_imdb)
        data = response.json()

        self.title.setText(f'Title: {data["Title"]}')
        self.year.setText(f'Year: {data["Year"]}')
        self.genre.setText(f'Genre: {data["Genre"]}')
        self.rating.setText(f'IMDB Rating: {data["imdbRating"]}')
        self.plot.setPlainText(data["Plot"])

        self.get_poster(data)
    def get_poster(self,data):
        poster_url=data["Poster"]
        response = requests.get(poster_url).content

        pixmap = QPixmap()
        pixmap.loadFromData(response)

        self.poster.setPixmap(pixmap.scaled(380,380, Qt.KeepAspectRatio))

    def display_error(self,message):
        pass

if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=SearchMovie()
    main.show()
    sys.exit(app.exec_())





