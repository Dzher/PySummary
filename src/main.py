import mainpanel.panelwindow as panel

import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = panel.PanelWindow()
    window.show()

    sys.exit(app.exec_())
