import sys
from PySide6.QtWidgets import QApplication, QMainWindow


class Showtimes(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)


if __name__ == "__main__":
    app = QApplication([])
    window = Showtimes()
    window.show()
    sys.exit(app.exec())
