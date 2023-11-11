from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Определить победителья')


but = QPushButton('Сгенерировать')
text = QLabel('Нажмиб чтобы унать победителья')
winner = QLabel('?')
line = QVBoxLayout()

line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(but, alignment = Qt.AlignCenter)
main_win.setLayout(line)

def show_winner():
    number = randint(0, 99)
    winner.setText(str(number))
    text.setText('Победитрель')

but.clicked.connect(show_winner)
main_win.show()
app.exec_()