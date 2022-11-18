import random
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QPixmap, QTransform, QImage, QColor, qRgba, qRed, qGreen, qBlue
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMainWindow, QGraphicsItem, QLabel, QInputDialog

SCREEN_SIZE = [500, 500]


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
        size = random.randrange(5, 300)
        qp.drawEllipse(random.randrange(0, 500), random.randrange(0, 500), size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())