import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QSlider,QFileDialog,QListWidget
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtMultimedia import QMediaPlayer,QAudioOutput

class Audio_app(QWidget):
    def __init__(self):
        super().__init__()
        self.folder_path=""
        self.setWindowTitle("SonicFlow")
        self.setGeometry(400, 100,600, 450)
        self.initUI()
        self.event_handler()

    def initUI(self):
        self.title=QLabel("SonicFlow")
        self.btn_choose=QPushButton('choose file')
        self.btn_play = QPushButton("play")
        self.btn_pause = QPushButton("pause")
        self.btn_resume = QPushButton("resume")
        self.btn_reset = QPushButton("reset")
        self.listWidget=QListWidget()

        self.btn_pause.setEnabled(False)
        self.btn_resume.setEnabled(False)
        self.btn_reset.setEnabled(False)

        self.slider=QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(50)
        self.slider.setMaximum(200)
        self.slider.setValue(100)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(10)

        self.slider_text=QLabel('Speed:1.00x')
        self.slider_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        slider_layout=QHBoxLayout()
        slider_layout.addWidget(self.slider)
        slider_layout.addWidget(self.slider_text)


        self.master=QVBoxLayout()
        row=QHBoxLayout()
        col1=QVBoxLayout()
        col2=QVBoxLayout()

        self.master.addWidget(self.title)
        self.master.addLayout(slider_layout)

        col1.addWidget(self.listWidget)
        col2.addWidget(self.btn_choose)
        col2.addWidget(self.btn_play)
        col2.addWidget(self.btn_pause)
        col2.addWidget(self.btn_resume)
        col2.addWidget(self.btn_reset)

        row.addLayout(col1,2)
        row.addLayout(col2,2)

        self.master.addLayout(row)
        self.setLayout(self.master)

        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.audio_output=QAudioOutput()
        self.media_player=QMediaPlayer()
        self.media_player.setAudioOutput(self.audio_output)

        self.title.setObjectName("title")
        self.slider.setObjectName("slider")

        self.setStyleSheet('''
        QWidget {
        background-color: rgb(7,10,25);
        }
        QPushButton {
        color:rgb(1,2,3);
        background-color: rgb(211,211,211);
        padding: 15px;
        border-radius: 6px;
        font-size: 15px;
        }
        QPushButton:hover {
        background-color: rgb(0,0,128);
        }
        QSlider{
        border-radius: 6px;}
        QLabel#title{
        font-size:14px;
        font-family:Arial;
        }
        ''')

    def event_handler(self):
        self.slider.valueChanged.connect(self.update_slider)
        self.btn_choose.clicked.connect(self.open_file)
        self.btn_play.clicked.connect(self.play)
        self.btn_pause.clicked.connect(self.pause)
        self.btn_resume.clicked.connect(self.resume)
        self.btn_reset.clicked.connect(self.reset)

    def update_slider(self):
        speed=self.slider.value()/100
        self.slider_text.setText(f'Speed :{speed:.2f}x')
        self.media_player.setPlaybackRate(speed)

    def play(self):
        if self.listWidget.selectedItems():
            self.title.setText('SonicFlow')
            file_name=self.listWidget.selectedItems()[0].text()
            file_path=os.path.join(self.folder_path,file_name)
            file_url=QUrl.fromLocalFile(file_path)

            self.media_player.setSource(file_url)
            self.media_player.setPlaybackRate(self.slider.value()/100.0)
            self.media_player.play()

            self.btn_play.setEnabled(True)
            self.btn_pause.setEnabled(True)
            self.btn_resume.setDisabled(True)
            self.btn_reset.setEnabled(True)
        else:
            if not self.listWidget.selectedItems():
                self.title.setText("⚠️ Select a file first")
                return

    def pause(self):
        self.media_player.pause()

        self.btn_play.setEnabled(True)
        self.btn_pause.setDisabled(True)
        self.btn_resume.setEnabled(True)
        self.btn_reset.setEnabled(True)
    def resume(self):
        self.media_player.play()

        self.btn_play.setEnabled(True)
        self.btn_pause.setEnabled(True)
        self.btn_resume.setDisabled(True)
        self.btn_reset.setEnabled(True)
    def reset(self):
        if self.media_player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.media_player.stop()

        self.media_player.setPosition(0)
        self.media_player.setPlaybackRate(self.slider.value()/100.0)
        self.media_player.play()

        self.btn_play.setEnabled(True)
        self.btn_pause.setEnabled(True)
        self.btn_resume.setDisabled(True)
        self.btn_reset.setEnabled(True)


    def open_file(self):
        path=QFileDialog.getExistingDirectory(self,'Select Folder')
        if path:
            self.folder_path=path
            self.listWidget.clear()
            for file_name in os.listdir(path):
                if file_name.endswith('.mp3'):
                    self.listWidget.addItem(file_name)
        else:
            file_name, _ = QFileDialog.getOpenFileName(
                self, 'Select File', filter='Audio files (*.mp3)')
            if file_name:
                self.folder_path = os.path.dirname(file_name)
                self.listWidget.clear()
                self.listWidget.addItem(os.path.basename(file_name))





if __name__=='__main__':
    app=QApplication(sys.argv)
    audio=Audio_app()
    audio.show()
    sys.exit(app.exec())
