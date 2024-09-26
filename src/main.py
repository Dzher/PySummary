import keyboard.keycounter as keycounter

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Summary")
    window.setMinimumSize(800, 450)
    desktop = QDesktopWidget()
    screen_rect = desktop.screenGeometry(0)
    window.move((screen_rect.width() - window.width()) // 2,
                (screen_rect.height() - window.height()) // 2)

    window.show()

    sys.exit(app.exec_())
