from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor
import sys
from random import randint


class OpenWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        radius = randint(50, 500)
        qp.drawEllipse(200, 200, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OpenWindow()
    ex.show()
    sys.exit(app.exec_())