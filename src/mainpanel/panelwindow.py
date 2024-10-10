from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QSystemTrayIcon, QMenu, QMenuBar, QAction, \
    QMessageBox
from PyQt5.QtCore import QTimer, QEvent
from src.keyboard.keycounterdlg import KeyCounterDlg


class PanelWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.key_counter_dlg = None
        self.tray_icon = None
        self.init_ui()
        self.init_menus()
        self.init_tray_icon()
        # TODO: run background should load from config settings
        self.run_background()

    def init_ui(self):
        self.setWindowIcon(QApplication.style().standardIcon(QApplication.style().SP_ComputerIcon))
        self.setWindowTitle('Summary')
        self.setMinimumSize(800, 450)
        desktop = QDesktopWidget()
        screen_rect = desktop.screenGeometry(0)
        self.move((screen_rect.width() - self.width()) / 2, (screen_rect.height() - self.height()) / 2)

    def init_menus(self):
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")
        quit_action = QAction("Quit", file_menu)
        quit_action.triggered.connect(self.close)
        file_menu.addAction(quit_action)

        start_menu = menu_bar.addMenu("Start")
        keyboard_action = QAction("KeyCounter", start_menu)
        keyboard_action.triggered.connect(self.show_key_counter)
        start_menu.addAction(keyboard_action)

        setting_menu = menu_bar.addMenu("Setting")
        setting_edit_action = QAction("Edit", setting_menu)
        setting_menu.addAction(setting_edit_action)

    def init_tray_icon(self):
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QApplication.style().standardIcon(QApplication.style().SP_ComputerIcon))

        tray_icon_menu = QMenu()
        restore_action = QAction("Restore", tray_icon_menu)
        restore_action.triggered.connect(self.showNormal)
        quit_action = QAction("Quit", tray_icon_menu)
        quit_action.triggered.connect(self.close)

        statistics_menu = QMenu("Statistics", tray_icon_menu)
        keyboard_action = QAction("KeyCounter", tray_icon_menu)
        keyboard_action.triggered.connect(self.show_key_counter)
        statistics_menu.addAction(keyboard_action)

        tray_icon_menu.addAction(restore_action)
        tray_icon_menu.addSeparator()
        tray_icon_menu.addMenu(statistics_menu)
        tray_icon_menu.addSeparator()
        tray_icon_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_icon_menu)
        self.tray_icon.setToolTip("Summary")
        self.tray_icon.show()

    def run_background(self):
        self.key_counter_dlg = KeyCounterDlg(self)

    def show_key_counter(self):
        self.setCentralWidget(self.key_counter_dlg)
        self.key_counter_dlg.show()

    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if self.isMinimized():
                QTimer.singleShot(0, self.hide)
                self.tray_icon.showMessage("Minimized", "Summary is now minimized to tray.",
                                           QSystemTrayIcon.Information, 500)

        super().changeEvent(event)

    def closeEvent(self, event):
        result = QMessageBox.question(self, "Warning",
                                      "Are you sure you want exit?\nClick 'Yes' to exit and 'No' to hide.")
        if QMessageBox.No == result:
            self.hide()
            event.ignore()
        else:
            super().closeEvent(event)
